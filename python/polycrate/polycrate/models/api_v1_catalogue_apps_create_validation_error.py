from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_catalogue_apps_create_annotations_error_component import (
        ApiV1CatalogueAppsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_archived_at_error_component import (
        ApiV1CatalogueAppsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_archived_by_error_component import (
        ApiV1CatalogueAppsCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_archived_error_component import (
        ApiV1CatalogueAppsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_archived_reason_error_component import (
        ApiV1CatalogueAppsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_artifact_package_error_component import (
        ApiV1CatalogueAppsCreateArtifactPackageErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_claim_error_component import ApiV1CatalogueAppsCreateClaimErrorComponent
    from ..models.api_v1_catalogue_apps_create_created_by_component_error_component import (
        ApiV1CatalogueAppsCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_created_by_user_error_component import (
        ApiV1CatalogueAppsCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_criticality_error_component import (
        ApiV1CatalogueAppsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_debug_mode_error_component import (
        ApiV1CatalogueAppsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_dependencies_error_component import (
        ApiV1CatalogueAppsCreateDependenciesErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_display_name_error_component import (
        ApiV1CatalogueAppsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_draft_error_component import ApiV1CatalogueAppsCreateDraftErrorComponent
    from ..models.api_v1_catalogue_apps_create_git_repository_url_error_component import (
        ApiV1CatalogueAppsCreateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_ha_enabled_expression_error_component import (
        ApiV1CatalogueAppsCreateHaEnabledExpressionErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_is_new_error_component import ApiV1CatalogueAppsCreateIsNewErrorComponent
    from ..models.api_v1_catalogue_apps_create_kind_error_component import ApiV1CatalogueAppsCreateKindErrorComponent
    from ..models.api_v1_catalogue_apps_create_labels_error_component import (
        ApiV1CatalogueAppsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1CatalogueAppsCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_maintainer_id_error_component import (
        ApiV1CatalogueAppsCreateMaintainerIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_managed_by_content_type_error_component import (
        ApiV1CatalogueAppsCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_managed_by_object_id_error_component import (
        ApiV1CatalogueAppsCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_markdown_content_error_component import (
        ApiV1CatalogueAppsCreateMarkdownContentErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_modified_by_user_error_component import (
        ApiV1CatalogueAppsCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_name_error_component import ApiV1CatalogueAppsCreateNameErrorComponent
    from ..models.api_v1_catalogue_apps_create_non_field_errors_error_component import (
        ApiV1CatalogueAppsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_platform_dns_record_created_error_component import (
        ApiV1CatalogueAppsCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_platform_service_error_component import (
        ApiV1CatalogueAppsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_product_ha_id_error_component import (
        ApiV1CatalogueAppsCreateProductHaIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_product_regular_id_error_component import (
        ApiV1CatalogueAppsCreateProductRegularIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_provider_error_component import (
        ApiV1CatalogueAppsCreateProviderErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_provider_id_error_component import (
        ApiV1CatalogueAppsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_provider_reference_error_component import (
        ApiV1CatalogueAppsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_reconciliation_enabled_error_component import (
        ApiV1CatalogueAppsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_registry_url_error_component import (
        ApiV1CatalogueAppsCreateRegistryUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_releases_url_error_component import (
        ApiV1CatalogueAppsCreateReleasesUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_screenshot_error_component import (
        ApiV1CatalogueAppsCreateScreenshotErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_serial_number_error_component import (
        ApiV1CatalogueAppsCreateSerialNumberErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_short_description_error_component import (
        ApiV1CatalogueAppsCreateShortDescriptionErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_sla_availability_error_component import (
        ApiV1CatalogueAppsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_sla_target_error_component import (
        ApiV1CatalogueAppsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_sla_window_days_error_component import (
        ApiV1CatalogueAppsCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_slo_availability_error_component import (
        ApiV1CatalogueAppsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_slo_target_error_component import (
        ApiV1CatalogueAppsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_slo_window_days_error_component import (
        ApiV1CatalogueAppsCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_supports_ha_error_component import (
        ApiV1CatalogueAppsCreateSupportsHaErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_target_availability_error_component import (
        ApiV1CatalogueAppsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_tolerations_error_component import (
        ApiV1CatalogueAppsCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_create_tracked_app_version_error_component import (
        ApiV1CatalogueAppsCreateTrackedAppVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CatalogueAppsCreateValidationError")


@_attrs_define
class ApiV1CatalogueAppsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CatalogueAppsCreateAnnotationsErrorComponent |
            ApiV1CatalogueAppsCreateArchivedAtErrorComponent | ApiV1CatalogueAppsCreateArchivedByErrorComponent |
            ApiV1CatalogueAppsCreateArchivedErrorComponent | ApiV1CatalogueAppsCreateArchivedReasonErrorComponent |
            ApiV1CatalogueAppsCreateArtifactPackageErrorComponent | ApiV1CatalogueAppsCreateClaimErrorComponent |
            ApiV1CatalogueAppsCreateCreatedByComponentErrorComponent | ApiV1CatalogueAppsCreateCreatedByUserErrorComponent |
            ApiV1CatalogueAppsCreateCriticalityErrorComponent | ApiV1CatalogueAppsCreateDebugModeErrorComponent |
            ApiV1CatalogueAppsCreateDependenciesErrorComponent | ApiV1CatalogueAppsCreateDisplayNameErrorComponent |
            ApiV1CatalogueAppsCreateDraftErrorComponent | ApiV1CatalogueAppsCreateGitRepositoryUrlErrorComponent |
            ApiV1CatalogueAppsCreateHaEnabledExpressionErrorComponent | ApiV1CatalogueAppsCreateIsNewErrorComponent |
            ApiV1CatalogueAppsCreateKindErrorComponent | ApiV1CatalogueAppsCreateLabelsErrorComponent |
            ApiV1CatalogueAppsCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1CatalogueAppsCreateMaintainerIdErrorComponent | ApiV1CatalogueAppsCreateManagedByContentTypeErrorComponent
            | ApiV1CatalogueAppsCreateManagedByObjectIdErrorComponent |
            ApiV1CatalogueAppsCreateMarkdownContentErrorComponent | ApiV1CatalogueAppsCreateModifiedByUserErrorComponent |
            ApiV1CatalogueAppsCreateNameErrorComponent | ApiV1CatalogueAppsCreateNonFieldErrorsErrorComponent |
            ApiV1CatalogueAppsCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1CatalogueAppsCreatePlatformServiceErrorComponent | ApiV1CatalogueAppsCreateProductHaIdErrorComponent |
            ApiV1CatalogueAppsCreateProductRegularIdErrorComponent | ApiV1CatalogueAppsCreateProviderErrorComponent |
            ApiV1CatalogueAppsCreateProviderIdErrorComponent | ApiV1CatalogueAppsCreateProviderReferenceErrorComponent |
            ApiV1CatalogueAppsCreateReconciliationEnabledErrorComponent | ApiV1CatalogueAppsCreateRegistryUrlErrorComponent
            | ApiV1CatalogueAppsCreateReleasesUrlErrorComponent | ApiV1CatalogueAppsCreateScreenshotErrorComponent |
            ApiV1CatalogueAppsCreateSerialNumberErrorComponent | ApiV1CatalogueAppsCreateShortDescriptionErrorComponent |
            ApiV1CatalogueAppsCreateSlaAvailabilityErrorComponent | ApiV1CatalogueAppsCreateSlaTargetErrorComponent |
            ApiV1CatalogueAppsCreateSlaWindowDaysErrorComponent | ApiV1CatalogueAppsCreateSloAvailabilityErrorComponent |
            ApiV1CatalogueAppsCreateSloTargetErrorComponent | ApiV1CatalogueAppsCreateSloWindowDaysErrorComponent |
            ApiV1CatalogueAppsCreateSupportsHaErrorComponent | ApiV1CatalogueAppsCreateTargetAvailabilityErrorComponent |
            ApiV1CatalogueAppsCreateTolerationsErrorComponent | ApiV1CatalogueAppsCreateTrackedAppVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CatalogueAppsCreateAnnotationsErrorComponent
        | ApiV1CatalogueAppsCreateArchivedAtErrorComponent
        | ApiV1CatalogueAppsCreateArchivedByErrorComponent
        | ApiV1CatalogueAppsCreateArchivedErrorComponent
        | ApiV1CatalogueAppsCreateArchivedReasonErrorComponent
        | ApiV1CatalogueAppsCreateArtifactPackageErrorComponent
        | ApiV1CatalogueAppsCreateClaimErrorComponent
        | ApiV1CatalogueAppsCreateCreatedByComponentErrorComponent
        | ApiV1CatalogueAppsCreateCreatedByUserErrorComponent
        | ApiV1CatalogueAppsCreateCriticalityErrorComponent
        | ApiV1CatalogueAppsCreateDebugModeErrorComponent
        | ApiV1CatalogueAppsCreateDependenciesErrorComponent
        | ApiV1CatalogueAppsCreateDisplayNameErrorComponent
        | ApiV1CatalogueAppsCreateDraftErrorComponent
        | ApiV1CatalogueAppsCreateGitRepositoryUrlErrorComponent
        | ApiV1CatalogueAppsCreateHaEnabledExpressionErrorComponent
        | ApiV1CatalogueAppsCreateIsNewErrorComponent
        | ApiV1CatalogueAppsCreateKindErrorComponent
        | ApiV1CatalogueAppsCreateLabelsErrorComponent
        | ApiV1CatalogueAppsCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1CatalogueAppsCreateMaintainerIdErrorComponent
        | ApiV1CatalogueAppsCreateManagedByContentTypeErrorComponent
        | ApiV1CatalogueAppsCreateManagedByObjectIdErrorComponent
        | ApiV1CatalogueAppsCreateMarkdownContentErrorComponent
        | ApiV1CatalogueAppsCreateModifiedByUserErrorComponent
        | ApiV1CatalogueAppsCreateNameErrorComponent
        | ApiV1CatalogueAppsCreateNonFieldErrorsErrorComponent
        | ApiV1CatalogueAppsCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1CatalogueAppsCreatePlatformServiceErrorComponent
        | ApiV1CatalogueAppsCreateProductHaIdErrorComponent
        | ApiV1CatalogueAppsCreateProductRegularIdErrorComponent
        | ApiV1CatalogueAppsCreateProviderErrorComponent
        | ApiV1CatalogueAppsCreateProviderIdErrorComponent
        | ApiV1CatalogueAppsCreateProviderReferenceErrorComponent
        | ApiV1CatalogueAppsCreateReconciliationEnabledErrorComponent
        | ApiV1CatalogueAppsCreateRegistryUrlErrorComponent
        | ApiV1CatalogueAppsCreateReleasesUrlErrorComponent
        | ApiV1CatalogueAppsCreateScreenshotErrorComponent
        | ApiV1CatalogueAppsCreateSerialNumberErrorComponent
        | ApiV1CatalogueAppsCreateShortDescriptionErrorComponent
        | ApiV1CatalogueAppsCreateSlaAvailabilityErrorComponent
        | ApiV1CatalogueAppsCreateSlaTargetErrorComponent
        | ApiV1CatalogueAppsCreateSlaWindowDaysErrorComponent
        | ApiV1CatalogueAppsCreateSloAvailabilityErrorComponent
        | ApiV1CatalogueAppsCreateSloTargetErrorComponent
        | ApiV1CatalogueAppsCreateSloWindowDaysErrorComponent
        | ApiV1CatalogueAppsCreateSupportsHaErrorComponent
        | ApiV1CatalogueAppsCreateTargetAvailabilityErrorComponent
        | ApiV1CatalogueAppsCreateTolerationsErrorComponent
        | ApiV1CatalogueAppsCreateTrackedAppVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_catalogue_apps_create_annotations_error_component import (
            ApiV1CatalogueAppsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_archived_at_error_component import (
            ApiV1CatalogueAppsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_archived_by_error_component import (
            ApiV1CatalogueAppsCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_archived_error_component import (
            ApiV1CatalogueAppsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_archived_reason_error_component import (
            ApiV1CatalogueAppsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_artifact_package_error_component import (
            ApiV1CatalogueAppsCreateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_claim_error_component import (
            ApiV1CatalogueAppsCreateClaimErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_created_by_component_error_component import (
            ApiV1CatalogueAppsCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_created_by_user_error_component import (
            ApiV1CatalogueAppsCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_criticality_error_component import (
            ApiV1CatalogueAppsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_debug_mode_error_component import (
            ApiV1CatalogueAppsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_display_name_error_component import (
            ApiV1CatalogueAppsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_draft_error_component import (
            ApiV1CatalogueAppsCreateDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_git_repository_url_error_component import (
            ApiV1CatalogueAppsCreateGitRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_ha_enabled_expression_error_component import (
            ApiV1CatalogueAppsCreateHaEnabledExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_is_new_error_component import (
            ApiV1CatalogueAppsCreateIsNewErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_kind_error_component import (
            ApiV1CatalogueAppsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_labels_error_component import (
            ApiV1CatalogueAppsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1CatalogueAppsCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_maintainer_id_error_component import (
            ApiV1CatalogueAppsCreateMaintainerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_managed_by_content_type_error_component import (
            ApiV1CatalogueAppsCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_managed_by_object_id_error_component import (
            ApiV1CatalogueAppsCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_markdown_content_error_component import (
            ApiV1CatalogueAppsCreateMarkdownContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_modified_by_user_error_component import (
            ApiV1CatalogueAppsCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_name_error_component import (
            ApiV1CatalogueAppsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_non_field_errors_error_component import (
            ApiV1CatalogueAppsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_platform_dns_record_created_error_component import (
            ApiV1CatalogueAppsCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_platform_service_error_component import (
            ApiV1CatalogueAppsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_product_ha_id_error_component import (
            ApiV1CatalogueAppsCreateProductHaIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_product_regular_id_error_component import (
            ApiV1CatalogueAppsCreateProductRegularIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_provider_error_component import (
            ApiV1CatalogueAppsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_provider_id_error_component import (
            ApiV1CatalogueAppsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_provider_reference_error_component import (
            ApiV1CatalogueAppsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_reconciliation_enabled_error_component import (
            ApiV1CatalogueAppsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_registry_url_error_component import (
            ApiV1CatalogueAppsCreateRegistryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_releases_url_error_component import (
            ApiV1CatalogueAppsCreateReleasesUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_screenshot_error_component import (
            ApiV1CatalogueAppsCreateScreenshotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_serial_number_error_component import (
            ApiV1CatalogueAppsCreateSerialNumberErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_short_description_error_component import (
            ApiV1CatalogueAppsCreateShortDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_sla_availability_error_component import (
            ApiV1CatalogueAppsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_sla_target_error_component import (
            ApiV1CatalogueAppsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_sla_window_days_error_component import (
            ApiV1CatalogueAppsCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_slo_availability_error_component import (
            ApiV1CatalogueAppsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_slo_target_error_component import (
            ApiV1CatalogueAppsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_slo_window_days_error_component import (
            ApiV1CatalogueAppsCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_supports_ha_error_component import (
            ApiV1CatalogueAppsCreateSupportsHaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_target_availability_error_component import (
            ApiV1CatalogueAppsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_tolerations_error_component import (
            ApiV1CatalogueAppsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_tracked_app_version_error_component import (
            ApiV1CatalogueAppsCreateTrackedAppVersionErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CatalogueAppsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateProductRegularIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateProductHaIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateMaintainerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateSerialNumberErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateShortDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateClaimErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateIsNewErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateScreenshotErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateMarkdownContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateHaEnabledExpressionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateTrackedAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsCreateArtifactPackageErrorComponent):
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
        from ..models.api_v1_catalogue_apps_create_annotations_error_component import (
            ApiV1CatalogueAppsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_archived_at_error_component import (
            ApiV1CatalogueAppsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_archived_by_error_component import (
            ApiV1CatalogueAppsCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_archived_error_component import (
            ApiV1CatalogueAppsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_archived_reason_error_component import (
            ApiV1CatalogueAppsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_artifact_package_error_component import (
            ApiV1CatalogueAppsCreateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_claim_error_component import (
            ApiV1CatalogueAppsCreateClaimErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_created_by_component_error_component import (
            ApiV1CatalogueAppsCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_created_by_user_error_component import (
            ApiV1CatalogueAppsCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_criticality_error_component import (
            ApiV1CatalogueAppsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_debug_mode_error_component import (
            ApiV1CatalogueAppsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_dependencies_error_component import (
            ApiV1CatalogueAppsCreateDependenciesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_display_name_error_component import (
            ApiV1CatalogueAppsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_draft_error_component import (
            ApiV1CatalogueAppsCreateDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_git_repository_url_error_component import (
            ApiV1CatalogueAppsCreateGitRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_ha_enabled_expression_error_component import (
            ApiV1CatalogueAppsCreateHaEnabledExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_is_new_error_component import (
            ApiV1CatalogueAppsCreateIsNewErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_kind_error_component import (
            ApiV1CatalogueAppsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_labels_error_component import (
            ApiV1CatalogueAppsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1CatalogueAppsCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_maintainer_id_error_component import (
            ApiV1CatalogueAppsCreateMaintainerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_managed_by_content_type_error_component import (
            ApiV1CatalogueAppsCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_managed_by_object_id_error_component import (
            ApiV1CatalogueAppsCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_markdown_content_error_component import (
            ApiV1CatalogueAppsCreateMarkdownContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_modified_by_user_error_component import (
            ApiV1CatalogueAppsCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_name_error_component import (
            ApiV1CatalogueAppsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_non_field_errors_error_component import (
            ApiV1CatalogueAppsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_platform_dns_record_created_error_component import (
            ApiV1CatalogueAppsCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_platform_service_error_component import (
            ApiV1CatalogueAppsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_product_ha_id_error_component import (
            ApiV1CatalogueAppsCreateProductHaIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_product_regular_id_error_component import (
            ApiV1CatalogueAppsCreateProductRegularIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_provider_error_component import (
            ApiV1CatalogueAppsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_provider_id_error_component import (
            ApiV1CatalogueAppsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_provider_reference_error_component import (
            ApiV1CatalogueAppsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_reconciliation_enabled_error_component import (
            ApiV1CatalogueAppsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_registry_url_error_component import (
            ApiV1CatalogueAppsCreateRegistryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_releases_url_error_component import (
            ApiV1CatalogueAppsCreateReleasesUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_screenshot_error_component import (
            ApiV1CatalogueAppsCreateScreenshotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_serial_number_error_component import (
            ApiV1CatalogueAppsCreateSerialNumberErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_short_description_error_component import (
            ApiV1CatalogueAppsCreateShortDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_sla_availability_error_component import (
            ApiV1CatalogueAppsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_sla_target_error_component import (
            ApiV1CatalogueAppsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_sla_window_days_error_component import (
            ApiV1CatalogueAppsCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_slo_availability_error_component import (
            ApiV1CatalogueAppsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_slo_target_error_component import (
            ApiV1CatalogueAppsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_slo_window_days_error_component import (
            ApiV1CatalogueAppsCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_supports_ha_error_component import (
            ApiV1CatalogueAppsCreateSupportsHaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_target_availability_error_component import (
            ApiV1CatalogueAppsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_tolerations_error_component import (
            ApiV1CatalogueAppsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_create_tracked_app_version_error_component import (
            ApiV1CatalogueAppsCreateTrackedAppVersionErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CatalogueAppsCreateAnnotationsErrorComponent
                | ApiV1CatalogueAppsCreateArchivedAtErrorComponent
                | ApiV1CatalogueAppsCreateArchivedByErrorComponent
                | ApiV1CatalogueAppsCreateArchivedErrorComponent
                | ApiV1CatalogueAppsCreateArchivedReasonErrorComponent
                | ApiV1CatalogueAppsCreateArtifactPackageErrorComponent
                | ApiV1CatalogueAppsCreateClaimErrorComponent
                | ApiV1CatalogueAppsCreateCreatedByComponentErrorComponent
                | ApiV1CatalogueAppsCreateCreatedByUserErrorComponent
                | ApiV1CatalogueAppsCreateCriticalityErrorComponent
                | ApiV1CatalogueAppsCreateDebugModeErrorComponent
                | ApiV1CatalogueAppsCreateDependenciesErrorComponent
                | ApiV1CatalogueAppsCreateDisplayNameErrorComponent
                | ApiV1CatalogueAppsCreateDraftErrorComponent
                | ApiV1CatalogueAppsCreateGitRepositoryUrlErrorComponent
                | ApiV1CatalogueAppsCreateHaEnabledExpressionErrorComponent
                | ApiV1CatalogueAppsCreateIsNewErrorComponent
                | ApiV1CatalogueAppsCreateKindErrorComponent
                | ApiV1CatalogueAppsCreateLabelsErrorComponent
                | ApiV1CatalogueAppsCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1CatalogueAppsCreateMaintainerIdErrorComponent
                | ApiV1CatalogueAppsCreateManagedByContentTypeErrorComponent
                | ApiV1CatalogueAppsCreateManagedByObjectIdErrorComponent
                | ApiV1CatalogueAppsCreateMarkdownContentErrorComponent
                | ApiV1CatalogueAppsCreateModifiedByUserErrorComponent
                | ApiV1CatalogueAppsCreateNameErrorComponent
                | ApiV1CatalogueAppsCreateNonFieldErrorsErrorComponent
                | ApiV1CatalogueAppsCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1CatalogueAppsCreatePlatformServiceErrorComponent
                | ApiV1CatalogueAppsCreateProductHaIdErrorComponent
                | ApiV1CatalogueAppsCreateProductRegularIdErrorComponent
                | ApiV1CatalogueAppsCreateProviderErrorComponent
                | ApiV1CatalogueAppsCreateProviderIdErrorComponent
                | ApiV1CatalogueAppsCreateProviderReferenceErrorComponent
                | ApiV1CatalogueAppsCreateReconciliationEnabledErrorComponent
                | ApiV1CatalogueAppsCreateRegistryUrlErrorComponent
                | ApiV1CatalogueAppsCreateReleasesUrlErrorComponent
                | ApiV1CatalogueAppsCreateScreenshotErrorComponent
                | ApiV1CatalogueAppsCreateSerialNumberErrorComponent
                | ApiV1CatalogueAppsCreateShortDescriptionErrorComponent
                | ApiV1CatalogueAppsCreateSlaAvailabilityErrorComponent
                | ApiV1CatalogueAppsCreateSlaTargetErrorComponent
                | ApiV1CatalogueAppsCreateSlaWindowDaysErrorComponent
                | ApiV1CatalogueAppsCreateSloAvailabilityErrorComponent
                | ApiV1CatalogueAppsCreateSloTargetErrorComponent
                | ApiV1CatalogueAppsCreateSloWindowDaysErrorComponent
                | ApiV1CatalogueAppsCreateSupportsHaErrorComponent
                | ApiV1CatalogueAppsCreateTargetAvailabilityErrorComponent
                | ApiV1CatalogueAppsCreateTolerationsErrorComponent
                | ApiV1CatalogueAppsCreateTrackedAppVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_0 = (
                        ApiV1CatalogueAppsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_1 = (
                        ApiV1CatalogueAppsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_2 = (
                        ApiV1CatalogueAppsCreateProductRegularIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_3 = (
                        ApiV1CatalogueAppsCreateProductHaIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_4 = (
                        ApiV1CatalogueAppsCreateMaintainerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_5 = (
                        ApiV1CatalogueAppsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_6 = (
                        ApiV1CatalogueAppsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_7 = (
                        ApiV1CatalogueAppsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_8 = (
                        ApiV1CatalogueAppsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_9 = (
                        ApiV1CatalogueAppsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_10 = (
                        ApiV1CatalogueAppsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_11 = (
                        ApiV1CatalogueAppsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_12 = (
                        ApiV1CatalogueAppsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_13 = (
                        ApiV1CatalogueAppsCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_14 = (
                        ApiV1CatalogueAppsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_15 = (
                        ApiV1CatalogueAppsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_16 = (
                        ApiV1CatalogueAppsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_17 = (
                        ApiV1CatalogueAppsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_18 = (
                        ApiV1CatalogueAppsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_19 = (
                        ApiV1CatalogueAppsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_20 = (
                        ApiV1CatalogueAppsCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_21 = (
                        ApiV1CatalogueAppsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_22 = (
                        ApiV1CatalogueAppsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_23 = (
                        ApiV1CatalogueAppsCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_24 = (
                        ApiV1CatalogueAppsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_25 = (
                        ApiV1CatalogueAppsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_26 = (
                        ApiV1CatalogueAppsCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_27 = (
                        ApiV1CatalogueAppsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_28 = (
                        ApiV1CatalogueAppsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_29 = (
                        ApiV1CatalogueAppsCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_30 = (
                        ApiV1CatalogueAppsCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_31 = (
                        ApiV1CatalogueAppsCreateSerialNumberErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_32 = (
                        ApiV1CatalogueAppsCreateShortDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_33 = (
                        ApiV1CatalogueAppsCreateClaimErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_34 = (
                        ApiV1CatalogueAppsCreateDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_35 = (
                        ApiV1CatalogueAppsCreateIsNewErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_36 = (
                        ApiV1CatalogueAppsCreateScreenshotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_37 = (
                        ApiV1CatalogueAppsCreateMarkdownContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_38 = (
                        ApiV1CatalogueAppsCreateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_39 = (
                        ApiV1CatalogueAppsCreateHaEnabledExpressionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_40 = (
                        ApiV1CatalogueAppsCreateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_41 = (
                        ApiV1CatalogueAppsCreateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_42 = (
                        ApiV1CatalogueAppsCreateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_43 = (
                        ApiV1CatalogueAppsCreateTrackedAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_44 = (
                        ApiV1CatalogueAppsCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_45 = (
                        ApiV1CatalogueAppsCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_46 = (
                        ApiV1CatalogueAppsCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_47 = (
                        ApiV1CatalogueAppsCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_create_error_type_48 = (
                        ApiV1CatalogueAppsCreateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_catalogue_apps_create_error_type_49 = (
                    ApiV1CatalogueAppsCreateDependenciesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_catalogue_apps_create_error_type_49

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_catalogue_apps_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_catalogue_apps_create_validation_error.additional_properties = d
        return api_v1_catalogue_apps_create_validation_error

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
