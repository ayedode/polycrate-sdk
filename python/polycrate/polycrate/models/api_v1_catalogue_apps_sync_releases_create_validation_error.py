from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_catalogue_apps_sync_releases_create_annotations_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_archived_at_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_archived_by_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_archived_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_archived_reason_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_artifact_package_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateArtifactPackageErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_claim_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateClaimErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_created_by_component_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_created_by_user_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_criticality_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_debug_mode_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_dependencies_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateDependenciesErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_display_name_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_draft_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateDraftErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_git_repository_url_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_ha_enabled_expression_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateHaEnabledExpressionErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_is_new_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateIsNewErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_kind_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateKindErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_labels_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_managed_by_content_type_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_managed_by_object_id_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_markdown_content_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateMarkdownContentErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_modified_by_user_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_name_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateNameErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_non_field_errors_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_platform_dns_record_created_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_platform_service_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_product_ha_id_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateProductHaIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_product_regular_id_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateProductRegularIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_provider_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateProviderErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_provider_id_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_provider_reference_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_reconciliation_enabled_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_registry_url_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateRegistryUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_releases_url_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateReleasesUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_screenshot_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateScreenshotErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_serial_number_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateSerialNumberErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_short_description_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateShortDescriptionErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_sla_availability_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_sla_target_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_sla_window_days_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_slo_availability_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_slo_target_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_slo_window_days_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_supports_ha_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateSupportsHaErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_target_availability_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_tolerations_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_sync_releases_create_tracked_app_version_error_component import (
        ApiV1CatalogueAppsSyncReleasesCreateTrackedAppVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CatalogueAppsSyncReleasesCreateValidationError")


@_attrs_define
class ApiV1CatalogueAppsSyncReleasesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CatalogueAppsSyncReleasesCreateAnnotationsErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateArchivedAtErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateArchivedByErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateArchivedErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateArchivedReasonErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateArtifactPackageErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateClaimErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateCreatedByComponentErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateCreatedByUserErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateCriticalityErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateDebugModeErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateDependenciesErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateDisplayNameErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateDraftErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateGitRepositoryUrlErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateHaEnabledExpressionErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateIsNewErrorComponent | ApiV1CatalogueAppsSyncReleasesCreateKindErrorComponent
            | ApiV1CatalogueAppsSyncReleasesCreateLabelsErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateManagedByContentTypeErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateManagedByObjectIdErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateMarkdownContentErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateModifiedByUserErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateNameErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateNonFieldErrorsErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreatePlatformServiceErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateProductHaIdErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateProductRegularIdErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateProviderErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateProviderIdErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateProviderReferenceErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateReconciliationEnabledErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateRegistryUrlErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateReleasesUrlErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateScreenshotErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateSerialNumberErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateShortDescriptionErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateSlaAvailabilityErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateSlaTargetErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateSlaWindowDaysErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateSloAvailabilityErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateSloTargetErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateSloWindowDaysErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateSupportsHaErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateTargetAvailabilityErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateTolerationsErrorComponent |
            ApiV1CatalogueAppsSyncReleasesCreateTrackedAppVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CatalogueAppsSyncReleasesCreateAnnotationsErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateArchivedAtErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateArchivedByErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateArchivedErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateArchivedReasonErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateArtifactPackageErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateClaimErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateCreatedByComponentErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateCreatedByUserErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateCriticalityErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateDebugModeErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateDependenciesErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateDisplayNameErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateDraftErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateGitRepositoryUrlErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateHaEnabledExpressionErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateIsNewErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateKindErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateLabelsErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateManagedByContentTypeErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateManagedByObjectIdErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateMarkdownContentErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateModifiedByUserErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateNameErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateNonFieldErrorsErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreatePlatformServiceErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateProductHaIdErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateProductRegularIdErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateProviderErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateProviderIdErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateProviderReferenceErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateReconciliationEnabledErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateRegistryUrlErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateReleasesUrlErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateScreenshotErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateSerialNumberErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateShortDescriptionErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateSlaAvailabilityErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateSlaTargetErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateSlaWindowDaysErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateSloAvailabilityErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateSloTargetErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateSloWindowDaysErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateSupportsHaErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateTargetAvailabilityErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateTolerationsErrorComponent
        | ApiV1CatalogueAppsSyncReleasesCreateTrackedAppVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_catalogue_apps_sync_releases_create_annotations_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_archived_at_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_archived_by_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_archived_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_archived_reason_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_artifact_package_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateArtifactPackageErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_claim_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateClaimErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_created_by_component_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_created_by_user_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_criticality_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_debug_mode_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_display_name_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_draft_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateDraftErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_git_repository_url_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_ha_enabled_expression_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateHaEnabledExpressionErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_is_new_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateIsNewErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_kind_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateKindErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_labels_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_managed_by_content_type_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_managed_by_object_id_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_markdown_content_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateMarkdownContentErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_modified_by_user_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_name_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateNameErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_non_field_errors_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_platform_dns_record_created_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_platform_service_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_product_ha_id_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateProductHaIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_product_regular_id_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateProductRegularIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_provider_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateProviderErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_provider_id_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_provider_reference_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_reconciliation_enabled_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_registry_url_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_releases_url_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_screenshot_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateScreenshotErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_serial_number_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSerialNumberErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_short_description_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateShortDescriptionErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_sla_availability_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_sla_target_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_sla_window_days_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_slo_availability_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_slo_target_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_slo_window_days_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_supports_ha_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSupportsHaErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_target_availability_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_tolerations_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_tracked_app_version_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateTrackedAppVersionErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateProductRegularIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateProductHaIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1CatalogueAppsSyncReleasesCreatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateSerialNumberErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateShortDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateClaimErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateIsNewErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateScreenshotErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateMarkdownContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateHaEnabledExpressionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateTrackedAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsSyncReleasesCreateArtifactPackageErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_catalogue_apps_sync_releases_create_annotations_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_archived_at_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_archived_by_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_archived_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_archived_reason_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_artifact_package_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateArtifactPackageErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_claim_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateClaimErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_created_by_component_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_created_by_user_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_criticality_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_debug_mode_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_dependencies_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateDependenciesErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_display_name_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_draft_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateDraftErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_git_repository_url_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_ha_enabled_expression_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateHaEnabledExpressionErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_is_new_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateIsNewErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_kind_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateKindErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_labels_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_managed_by_content_type_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_managed_by_object_id_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_markdown_content_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateMarkdownContentErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_modified_by_user_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_name_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateNameErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_non_field_errors_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_platform_dns_record_created_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_platform_service_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_product_ha_id_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateProductHaIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_product_regular_id_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateProductRegularIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_provider_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateProviderErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_provider_id_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_provider_reference_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_reconciliation_enabled_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_registry_url_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_releases_url_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_screenshot_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateScreenshotErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_serial_number_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSerialNumberErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_short_description_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateShortDescriptionErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_sla_availability_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_sla_target_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_sla_window_days_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_slo_availability_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_slo_target_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_slo_window_days_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_supports_ha_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateSupportsHaErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_target_availability_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_tolerations_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_sync_releases_create_tracked_app_version_error_component import (
            ApiV1CatalogueAppsSyncReleasesCreateTrackedAppVersionErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CatalogueAppsSyncReleasesCreateAnnotationsErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateArchivedAtErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateArchivedByErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateArchivedErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateArchivedReasonErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateArtifactPackageErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateClaimErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateCreatedByComponentErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateCreatedByUserErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateCriticalityErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateDebugModeErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateDependenciesErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateDisplayNameErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateDraftErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateGitRepositoryUrlErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateHaEnabledExpressionErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateIsNewErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateKindErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateLabelsErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateManagedByContentTypeErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateManagedByObjectIdErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateMarkdownContentErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateModifiedByUserErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateNameErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateNonFieldErrorsErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreatePlatformServiceErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateProductHaIdErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateProductRegularIdErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateProviderErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateProviderIdErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateProviderReferenceErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateReconciliationEnabledErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateRegistryUrlErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateReleasesUrlErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateScreenshotErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateSerialNumberErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateShortDescriptionErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateSlaAvailabilityErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateSlaTargetErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateSlaWindowDaysErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateSloAvailabilityErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateSloTargetErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateSloWindowDaysErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateSupportsHaErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateTargetAvailabilityErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateTolerationsErrorComponent
                | ApiV1CatalogueAppsSyncReleasesCreateTrackedAppVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_0 = (
                        ApiV1CatalogueAppsSyncReleasesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_1 = (
                        ApiV1CatalogueAppsSyncReleasesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_2 = (
                        ApiV1CatalogueAppsSyncReleasesCreateProductRegularIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_3 = (
                        ApiV1CatalogueAppsSyncReleasesCreateProductHaIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_4 = (
                        ApiV1CatalogueAppsSyncReleasesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_5 = (
                        ApiV1CatalogueAppsSyncReleasesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_6 = (
                        ApiV1CatalogueAppsSyncReleasesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_7 = (
                        ApiV1CatalogueAppsSyncReleasesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_8 = (
                        ApiV1CatalogueAppsSyncReleasesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_9 = (
                        ApiV1CatalogueAppsSyncReleasesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_10 = (
                        ApiV1CatalogueAppsSyncReleasesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_11 = (
                        ApiV1CatalogueAppsSyncReleasesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_12 = (
                        ApiV1CatalogueAppsSyncReleasesCreateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_13 = (
                        ApiV1CatalogueAppsSyncReleasesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_14 = (
                        ApiV1CatalogueAppsSyncReleasesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_15 = (
                        ApiV1CatalogueAppsSyncReleasesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_16 = (
                        ApiV1CatalogueAppsSyncReleasesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_17 = (
                        ApiV1CatalogueAppsSyncReleasesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_18 = (
                        ApiV1CatalogueAppsSyncReleasesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_19 = (
                        ApiV1CatalogueAppsSyncReleasesCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_20 = (
                        ApiV1CatalogueAppsSyncReleasesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_21 = (
                        ApiV1CatalogueAppsSyncReleasesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_22 = (
                        ApiV1CatalogueAppsSyncReleasesCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_23 = (
                        ApiV1CatalogueAppsSyncReleasesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_24 = (
                        ApiV1CatalogueAppsSyncReleasesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_25 = (
                        ApiV1CatalogueAppsSyncReleasesCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_26 = (
                        ApiV1CatalogueAppsSyncReleasesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_27 = (
                        ApiV1CatalogueAppsSyncReleasesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_28 = (
                        ApiV1CatalogueAppsSyncReleasesCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_29 = (
                        ApiV1CatalogueAppsSyncReleasesCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_30 = (
                        ApiV1CatalogueAppsSyncReleasesCreateSerialNumberErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_31 = (
                        ApiV1CatalogueAppsSyncReleasesCreateShortDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_32 = (
                        ApiV1CatalogueAppsSyncReleasesCreateClaimErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_33 = (
                        ApiV1CatalogueAppsSyncReleasesCreateDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_34 = (
                        ApiV1CatalogueAppsSyncReleasesCreateIsNewErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_35 = (
                        ApiV1CatalogueAppsSyncReleasesCreateScreenshotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_36 = (
                        ApiV1CatalogueAppsSyncReleasesCreateMarkdownContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_37 = (
                        ApiV1CatalogueAppsSyncReleasesCreateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_38 = (
                        ApiV1CatalogueAppsSyncReleasesCreateHaEnabledExpressionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_39 = (
                        ApiV1CatalogueAppsSyncReleasesCreateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_40 = (
                        ApiV1CatalogueAppsSyncReleasesCreateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_41 = (
                        ApiV1CatalogueAppsSyncReleasesCreateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_42 = (
                        ApiV1CatalogueAppsSyncReleasesCreateTrackedAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_43 = (
                        ApiV1CatalogueAppsSyncReleasesCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_44 = (
                        ApiV1CatalogueAppsSyncReleasesCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_45 = (
                        ApiV1CatalogueAppsSyncReleasesCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_46 = (
                        ApiV1CatalogueAppsSyncReleasesCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_47 = (
                        ApiV1CatalogueAppsSyncReleasesCreateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_48 = (
                    ApiV1CatalogueAppsSyncReleasesCreateDependenciesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_catalogue_apps_sync_releases_create_error_type_48

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_catalogue_apps_sync_releases_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_catalogue_apps_sync_releases_create_validation_error.additional_properties = d
        return api_v1_catalogue_apps_sync_releases_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
