from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_catalogue_apps_archive_create_annotations_error_component import (
        ApiV1CatalogueAppsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_archived_at_error_component import (
        ApiV1CatalogueAppsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_archived_by_error_component import (
        ApiV1CatalogueAppsArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_archived_error_component import (
        ApiV1CatalogueAppsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_archived_reason_error_component import (
        ApiV1CatalogueAppsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_artifact_package_error_component import (
        ApiV1CatalogueAppsArchiveCreateArtifactPackageErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_claim_error_component import (
        ApiV1CatalogueAppsArchiveCreateClaimErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_created_by_component_error_component import (
        ApiV1CatalogueAppsArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_created_by_user_error_component import (
        ApiV1CatalogueAppsArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_criticality_error_component import (
        ApiV1CatalogueAppsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_debug_mode_error_component import (
        ApiV1CatalogueAppsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_dependencies_error_component import (
        ApiV1CatalogueAppsArchiveCreateDependenciesErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_display_name_error_component import (
        ApiV1CatalogueAppsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_draft_error_component import (
        ApiV1CatalogueAppsArchiveCreateDraftErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_git_repository_url_error_component import (
        ApiV1CatalogueAppsArchiveCreateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_ha_enabled_expression_error_component import (
        ApiV1CatalogueAppsArchiveCreateHaEnabledExpressionErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_is_new_error_component import (
        ApiV1CatalogueAppsArchiveCreateIsNewErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_kind_error_component import (
        ApiV1CatalogueAppsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_labels_error_component import (
        ApiV1CatalogueAppsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1CatalogueAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_maintainer_id_error_component import (
        ApiV1CatalogueAppsArchiveCreateMaintainerIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_managed_by_content_type_error_component import (
        ApiV1CatalogueAppsArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_managed_by_object_id_error_component import (
        ApiV1CatalogueAppsArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_markdown_content_error_component import (
        ApiV1CatalogueAppsArchiveCreateMarkdownContentErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_modified_by_user_error_component import (
        ApiV1CatalogueAppsArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_name_error_component import (
        ApiV1CatalogueAppsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_non_field_errors_error_component import (
        ApiV1CatalogueAppsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_platform_dns_record_created_error_component import (
        ApiV1CatalogueAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_platform_service_error_component import (
        ApiV1CatalogueAppsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_product_ha_id_error_component import (
        ApiV1CatalogueAppsArchiveCreateProductHaIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_product_regular_id_error_component import (
        ApiV1CatalogueAppsArchiveCreateProductRegularIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_provider_error_component import (
        ApiV1CatalogueAppsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_provider_id_error_component import (
        ApiV1CatalogueAppsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_provider_reference_error_component import (
        ApiV1CatalogueAppsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_reconciliation_enabled_error_component import (
        ApiV1CatalogueAppsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_registry_url_error_component import (
        ApiV1CatalogueAppsArchiveCreateRegistryUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_releases_url_error_component import (
        ApiV1CatalogueAppsArchiveCreateReleasesUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_screenshot_error_component import (
        ApiV1CatalogueAppsArchiveCreateScreenshotErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_serial_number_error_component import (
        ApiV1CatalogueAppsArchiveCreateSerialNumberErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_short_description_error_component import (
        ApiV1CatalogueAppsArchiveCreateShortDescriptionErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_sla_availability_error_component import (
        ApiV1CatalogueAppsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_sla_target_error_component import (
        ApiV1CatalogueAppsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_sla_window_days_error_component import (
        ApiV1CatalogueAppsArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_slo_availability_error_component import (
        ApiV1CatalogueAppsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_slo_target_error_component import (
        ApiV1CatalogueAppsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_slo_window_days_error_component import (
        ApiV1CatalogueAppsArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_supports_ha_error_component import (
        ApiV1CatalogueAppsArchiveCreateSupportsHaErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_target_availability_error_component import (
        ApiV1CatalogueAppsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_tolerations_error_component import (
        ApiV1CatalogueAppsArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_archive_create_tracked_app_version_error_component import (
        ApiV1CatalogueAppsArchiveCreateTrackedAppVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CatalogueAppsArchiveCreateValidationError")


@_attrs_define
class ApiV1CatalogueAppsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CatalogueAppsArchiveCreateAnnotationsErrorComponent |
            ApiV1CatalogueAppsArchiveCreateArchivedAtErrorComponent |
            ApiV1CatalogueAppsArchiveCreateArchivedByErrorComponent | ApiV1CatalogueAppsArchiveCreateArchivedErrorComponent
            | ApiV1CatalogueAppsArchiveCreateArchivedReasonErrorComponent |
            ApiV1CatalogueAppsArchiveCreateArtifactPackageErrorComponent |
            ApiV1CatalogueAppsArchiveCreateClaimErrorComponent |
            ApiV1CatalogueAppsArchiveCreateCreatedByComponentErrorComponent |
            ApiV1CatalogueAppsArchiveCreateCreatedByUserErrorComponent |
            ApiV1CatalogueAppsArchiveCreateCriticalityErrorComponent |
            ApiV1CatalogueAppsArchiveCreateDebugModeErrorComponent |
            ApiV1CatalogueAppsArchiveCreateDependenciesErrorComponent |
            ApiV1CatalogueAppsArchiveCreateDisplayNameErrorComponent | ApiV1CatalogueAppsArchiveCreateDraftErrorComponent |
            ApiV1CatalogueAppsArchiveCreateGitRepositoryUrlErrorComponent |
            ApiV1CatalogueAppsArchiveCreateHaEnabledExpressionErrorComponent |
            ApiV1CatalogueAppsArchiveCreateIsNewErrorComponent | ApiV1CatalogueAppsArchiveCreateKindErrorComponent |
            ApiV1CatalogueAppsArchiveCreateLabelsErrorComponent |
            ApiV1CatalogueAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1CatalogueAppsArchiveCreateMaintainerIdErrorComponent |
            ApiV1CatalogueAppsArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1CatalogueAppsArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1CatalogueAppsArchiveCreateMarkdownContentErrorComponent |
            ApiV1CatalogueAppsArchiveCreateModifiedByUserErrorComponent | ApiV1CatalogueAppsArchiveCreateNameErrorComponent
            | ApiV1CatalogueAppsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1CatalogueAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1CatalogueAppsArchiveCreatePlatformServiceErrorComponent |
            ApiV1CatalogueAppsArchiveCreateProductHaIdErrorComponent |
            ApiV1CatalogueAppsArchiveCreateProductRegularIdErrorComponent |
            ApiV1CatalogueAppsArchiveCreateProviderErrorComponent | ApiV1CatalogueAppsArchiveCreateProviderIdErrorComponent
            | ApiV1CatalogueAppsArchiveCreateProviderReferenceErrorComponent |
            ApiV1CatalogueAppsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1CatalogueAppsArchiveCreateRegistryUrlErrorComponent |
            ApiV1CatalogueAppsArchiveCreateReleasesUrlErrorComponent |
            ApiV1CatalogueAppsArchiveCreateScreenshotErrorComponent |
            ApiV1CatalogueAppsArchiveCreateSerialNumberErrorComponent |
            ApiV1CatalogueAppsArchiveCreateShortDescriptionErrorComponent |
            ApiV1CatalogueAppsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1CatalogueAppsArchiveCreateSlaTargetErrorComponent |
            ApiV1CatalogueAppsArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1CatalogueAppsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1CatalogueAppsArchiveCreateSloTargetErrorComponent |
            ApiV1CatalogueAppsArchiveCreateSloWindowDaysErrorComponent |
            ApiV1CatalogueAppsArchiveCreateSupportsHaErrorComponent |
            ApiV1CatalogueAppsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1CatalogueAppsArchiveCreateTolerationsErrorComponent |
            ApiV1CatalogueAppsArchiveCreateTrackedAppVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CatalogueAppsArchiveCreateAnnotationsErrorComponent
        | ApiV1CatalogueAppsArchiveCreateArchivedAtErrorComponent
        | ApiV1CatalogueAppsArchiveCreateArchivedByErrorComponent
        | ApiV1CatalogueAppsArchiveCreateArchivedErrorComponent
        | ApiV1CatalogueAppsArchiveCreateArchivedReasonErrorComponent
        | ApiV1CatalogueAppsArchiveCreateArtifactPackageErrorComponent
        | ApiV1CatalogueAppsArchiveCreateClaimErrorComponent
        | ApiV1CatalogueAppsArchiveCreateCreatedByComponentErrorComponent
        | ApiV1CatalogueAppsArchiveCreateCreatedByUserErrorComponent
        | ApiV1CatalogueAppsArchiveCreateCriticalityErrorComponent
        | ApiV1CatalogueAppsArchiveCreateDebugModeErrorComponent
        | ApiV1CatalogueAppsArchiveCreateDependenciesErrorComponent
        | ApiV1CatalogueAppsArchiveCreateDisplayNameErrorComponent
        | ApiV1CatalogueAppsArchiveCreateDraftErrorComponent
        | ApiV1CatalogueAppsArchiveCreateGitRepositoryUrlErrorComponent
        | ApiV1CatalogueAppsArchiveCreateHaEnabledExpressionErrorComponent
        | ApiV1CatalogueAppsArchiveCreateIsNewErrorComponent
        | ApiV1CatalogueAppsArchiveCreateKindErrorComponent
        | ApiV1CatalogueAppsArchiveCreateLabelsErrorComponent
        | ApiV1CatalogueAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1CatalogueAppsArchiveCreateMaintainerIdErrorComponent
        | ApiV1CatalogueAppsArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1CatalogueAppsArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1CatalogueAppsArchiveCreateMarkdownContentErrorComponent
        | ApiV1CatalogueAppsArchiveCreateModifiedByUserErrorComponent
        | ApiV1CatalogueAppsArchiveCreateNameErrorComponent
        | ApiV1CatalogueAppsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1CatalogueAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1CatalogueAppsArchiveCreatePlatformServiceErrorComponent
        | ApiV1CatalogueAppsArchiveCreateProductHaIdErrorComponent
        | ApiV1CatalogueAppsArchiveCreateProductRegularIdErrorComponent
        | ApiV1CatalogueAppsArchiveCreateProviderErrorComponent
        | ApiV1CatalogueAppsArchiveCreateProviderIdErrorComponent
        | ApiV1CatalogueAppsArchiveCreateProviderReferenceErrorComponent
        | ApiV1CatalogueAppsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1CatalogueAppsArchiveCreateRegistryUrlErrorComponent
        | ApiV1CatalogueAppsArchiveCreateReleasesUrlErrorComponent
        | ApiV1CatalogueAppsArchiveCreateScreenshotErrorComponent
        | ApiV1CatalogueAppsArchiveCreateSerialNumberErrorComponent
        | ApiV1CatalogueAppsArchiveCreateShortDescriptionErrorComponent
        | ApiV1CatalogueAppsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1CatalogueAppsArchiveCreateSlaTargetErrorComponent
        | ApiV1CatalogueAppsArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1CatalogueAppsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1CatalogueAppsArchiveCreateSloTargetErrorComponent
        | ApiV1CatalogueAppsArchiveCreateSloWindowDaysErrorComponent
        | ApiV1CatalogueAppsArchiveCreateSupportsHaErrorComponent
        | ApiV1CatalogueAppsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1CatalogueAppsArchiveCreateTolerationsErrorComponent
        | ApiV1CatalogueAppsArchiveCreateTrackedAppVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_catalogue_apps_archive_create_annotations_error_component import (
            ApiV1CatalogueAppsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_archived_at_error_component import (
            ApiV1CatalogueAppsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_archived_by_error_component import (
            ApiV1CatalogueAppsArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_archived_error_component import (
            ApiV1CatalogueAppsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_archived_reason_error_component import (
            ApiV1CatalogueAppsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_artifact_package_error_component import (
            ApiV1CatalogueAppsArchiveCreateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_claim_error_component import (
            ApiV1CatalogueAppsArchiveCreateClaimErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_created_by_component_error_component import (
            ApiV1CatalogueAppsArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_created_by_user_error_component import (
            ApiV1CatalogueAppsArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_criticality_error_component import (
            ApiV1CatalogueAppsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_debug_mode_error_component import (
            ApiV1CatalogueAppsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_display_name_error_component import (
            ApiV1CatalogueAppsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_draft_error_component import (
            ApiV1CatalogueAppsArchiveCreateDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_git_repository_url_error_component import (
            ApiV1CatalogueAppsArchiveCreateGitRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_ha_enabled_expression_error_component import (
            ApiV1CatalogueAppsArchiveCreateHaEnabledExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_is_new_error_component import (
            ApiV1CatalogueAppsArchiveCreateIsNewErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_kind_error_component import (
            ApiV1CatalogueAppsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_labels_error_component import (
            ApiV1CatalogueAppsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1CatalogueAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_maintainer_id_error_component import (
            ApiV1CatalogueAppsArchiveCreateMaintainerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_managed_by_content_type_error_component import (
            ApiV1CatalogueAppsArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_managed_by_object_id_error_component import (
            ApiV1CatalogueAppsArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_markdown_content_error_component import (
            ApiV1CatalogueAppsArchiveCreateMarkdownContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_modified_by_user_error_component import (
            ApiV1CatalogueAppsArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_name_error_component import (
            ApiV1CatalogueAppsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_non_field_errors_error_component import (
            ApiV1CatalogueAppsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_platform_dns_record_created_error_component import (
            ApiV1CatalogueAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_platform_service_error_component import (
            ApiV1CatalogueAppsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_product_ha_id_error_component import (
            ApiV1CatalogueAppsArchiveCreateProductHaIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_product_regular_id_error_component import (
            ApiV1CatalogueAppsArchiveCreateProductRegularIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_provider_error_component import (
            ApiV1CatalogueAppsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_provider_id_error_component import (
            ApiV1CatalogueAppsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_provider_reference_error_component import (
            ApiV1CatalogueAppsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_reconciliation_enabled_error_component import (
            ApiV1CatalogueAppsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_registry_url_error_component import (
            ApiV1CatalogueAppsArchiveCreateRegistryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_releases_url_error_component import (
            ApiV1CatalogueAppsArchiveCreateReleasesUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_screenshot_error_component import (
            ApiV1CatalogueAppsArchiveCreateScreenshotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_serial_number_error_component import (
            ApiV1CatalogueAppsArchiveCreateSerialNumberErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_short_description_error_component import (
            ApiV1CatalogueAppsArchiveCreateShortDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_sla_availability_error_component import (
            ApiV1CatalogueAppsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_sla_target_error_component import (
            ApiV1CatalogueAppsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_sla_window_days_error_component import (
            ApiV1CatalogueAppsArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_slo_availability_error_component import (
            ApiV1CatalogueAppsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_slo_target_error_component import (
            ApiV1CatalogueAppsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_slo_window_days_error_component import (
            ApiV1CatalogueAppsArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_supports_ha_error_component import (
            ApiV1CatalogueAppsArchiveCreateSupportsHaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_target_availability_error_component import (
            ApiV1CatalogueAppsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_tolerations_error_component import (
            ApiV1CatalogueAppsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_tracked_app_version_error_component import (
            ApiV1CatalogueAppsArchiveCreateTrackedAppVersionErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateProductRegularIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateProductHaIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateMaintainerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1CatalogueAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateSerialNumberErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateShortDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateClaimErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateIsNewErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateScreenshotErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateMarkdownContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateHaEnabledExpressionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateTrackedAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsArchiveCreateArtifactPackageErrorComponent):
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
        from ..models.api_v1_catalogue_apps_archive_create_annotations_error_component import (
            ApiV1CatalogueAppsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_archived_at_error_component import (
            ApiV1CatalogueAppsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_archived_by_error_component import (
            ApiV1CatalogueAppsArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_archived_error_component import (
            ApiV1CatalogueAppsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_archived_reason_error_component import (
            ApiV1CatalogueAppsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_artifact_package_error_component import (
            ApiV1CatalogueAppsArchiveCreateArtifactPackageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_claim_error_component import (
            ApiV1CatalogueAppsArchiveCreateClaimErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_created_by_component_error_component import (
            ApiV1CatalogueAppsArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_created_by_user_error_component import (
            ApiV1CatalogueAppsArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_criticality_error_component import (
            ApiV1CatalogueAppsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_debug_mode_error_component import (
            ApiV1CatalogueAppsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_dependencies_error_component import (
            ApiV1CatalogueAppsArchiveCreateDependenciesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_display_name_error_component import (
            ApiV1CatalogueAppsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_draft_error_component import (
            ApiV1CatalogueAppsArchiveCreateDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_git_repository_url_error_component import (
            ApiV1CatalogueAppsArchiveCreateGitRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_ha_enabled_expression_error_component import (
            ApiV1CatalogueAppsArchiveCreateHaEnabledExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_is_new_error_component import (
            ApiV1CatalogueAppsArchiveCreateIsNewErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_kind_error_component import (
            ApiV1CatalogueAppsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_labels_error_component import (
            ApiV1CatalogueAppsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1CatalogueAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_maintainer_id_error_component import (
            ApiV1CatalogueAppsArchiveCreateMaintainerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_managed_by_content_type_error_component import (
            ApiV1CatalogueAppsArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_managed_by_object_id_error_component import (
            ApiV1CatalogueAppsArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_markdown_content_error_component import (
            ApiV1CatalogueAppsArchiveCreateMarkdownContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_modified_by_user_error_component import (
            ApiV1CatalogueAppsArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_name_error_component import (
            ApiV1CatalogueAppsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_non_field_errors_error_component import (
            ApiV1CatalogueAppsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_platform_dns_record_created_error_component import (
            ApiV1CatalogueAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_platform_service_error_component import (
            ApiV1CatalogueAppsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_product_ha_id_error_component import (
            ApiV1CatalogueAppsArchiveCreateProductHaIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_product_regular_id_error_component import (
            ApiV1CatalogueAppsArchiveCreateProductRegularIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_provider_error_component import (
            ApiV1CatalogueAppsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_provider_id_error_component import (
            ApiV1CatalogueAppsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_provider_reference_error_component import (
            ApiV1CatalogueAppsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_reconciliation_enabled_error_component import (
            ApiV1CatalogueAppsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_registry_url_error_component import (
            ApiV1CatalogueAppsArchiveCreateRegistryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_releases_url_error_component import (
            ApiV1CatalogueAppsArchiveCreateReleasesUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_screenshot_error_component import (
            ApiV1CatalogueAppsArchiveCreateScreenshotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_serial_number_error_component import (
            ApiV1CatalogueAppsArchiveCreateSerialNumberErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_short_description_error_component import (
            ApiV1CatalogueAppsArchiveCreateShortDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_sla_availability_error_component import (
            ApiV1CatalogueAppsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_sla_target_error_component import (
            ApiV1CatalogueAppsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_sla_window_days_error_component import (
            ApiV1CatalogueAppsArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_slo_availability_error_component import (
            ApiV1CatalogueAppsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_slo_target_error_component import (
            ApiV1CatalogueAppsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_slo_window_days_error_component import (
            ApiV1CatalogueAppsArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_supports_ha_error_component import (
            ApiV1CatalogueAppsArchiveCreateSupportsHaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_target_availability_error_component import (
            ApiV1CatalogueAppsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_tolerations_error_component import (
            ApiV1CatalogueAppsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_catalogue_apps_archive_create_tracked_app_version_error_component import (
            ApiV1CatalogueAppsArchiveCreateTrackedAppVersionErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CatalogueAppsArchiveCreateAnnotationsErrorComponent
                | ApiV1CatalogueAppsArchiveCreateArchivedAtErrorComponent
                | ApiV1CatalogueAppsArchiveCreateArchivedByErrorComponent
                | ApiV1CatalogueAppsArchiveCreateArchivedErrorComponent
                | ApiV1CatalogueAppsArchiveCreateArchivedReasonErrorComponent
                | ApiV1CatalogueAppsArchiveCreateArtifactPackageErrorComponent
                | ApiV1CatalogueAppsArchiveCreateClaimErrorComponent
                | ApiV1CatalogueAppsArchiveCreateCreatedByComponentErrorComponent
                | ApiV1CatalogueAppsArchiveCreateCreatedByUserErrorComponent
                | ApiV1CatalogueAppsArchiveCreateCriticalityErrorComponent
                | ApiV1CatalogueAppsArchiveCreateDebugModeErrorComponent
                | ApiV1CatalogueAppsArchiveCreateDependenciesErrorComponent
                | ApiV1CatalogueAppsArchiveCreateDisplayNameErrorComponent
                | ApiV1CatalogueAppsArchiveCreateDraftErrorComponent
                | ApiV1CatalogueAppsArchiveCreateGitRepositoryUrlErrorComponent
                | ApiV1CatalogueAppsArchiveCreateHaEnabledExpressionErrorComponent
                | ApiV1CatalogueAppsArchiveCreateIsNewErrorComponent
                | ApiV1CatalogueAppsArchiveCreateKindErrorComponent
                | ApiV1CatalogueAppsArchiveCreateLabelsErrorComponent
                | ApiV1CatalogueAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1CatalogueAppsArchiveCreateMaintainerIdErrorComponent
                | ApiV1CatalogueAppsArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1CatalogueAppsArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1CatalogueAppsArchiveCreateMarkdownContentErrorComponent
                | ApiV1CatalogueAppsArchiveCreateModifiedByUserErrorComponent
                | ApiV1CatalogueAppsArchiveCreateNameErrorComponent
                | ApiV1CatalogueAppsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1CatalogueAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1CatalogueAppsArchiveCreatePlatformServiceErrorComponent
                | ApiV1CatalogueAppsArchiveCreateProductHaIdErrorComponent
                | ApiV1CatalogueAppsArchiveCreateProductRegularIdErrorComponent
                | ApiV1CatalogueAppsArchiveCreateProviderErrorComponent
                | ApiV1CatalogueAppsArchiveCreateProviderIdErrorComponent
                | ApiV1CatalogueAppsArchiveCreateProviderReferenceErrorComponent
                | ApiV1CatalogueAppsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1CatalogueAppsArchiveCreateRegistryUrlErrorComponent
                | ApiV1CatalogueAppsArchiveCreateReleasesUrlErrorComponent
                | ApiV1CatalogueAppsArchiveCreateScreenshotErrorComponent
                | ApiV1CatalogueAppsArchiveCreateSerialNumberErrorComponent
                | ApiV1CatalogueAppsArchiveCreateShortDescriptionErrorComponent
                | ApiV1CatalogueAppsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1CatalogueAppsArchiveCreateSlaTargetErrorComponent
                | ApiV1CatalogueAppsArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1CatalogueAppsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1CatalogueAppsArchiveCreateSloTargetErrorComponent
                | ApiV1CatalogueAppsArchiveCreateSloWindowDaysErrorComponent
                | ApiV1CatalogueAppsArchiveCreateSupportsHaErrorComponent
                | ApiV1CatalogueAppsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1CatalogueAppsArchiveCreateTolerationsErrorComponent
                | ApiV1CatalogueAppsArchiveCreateTrackedAppVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_0 = (
                        ApiV1CatalogueAppsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_1 = (
                        ApiV1CatalogueAppsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_2 = (
                        ApiV1CatalogueAppsArchiveCreateProductRegularIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_3 = (
                        ApiV1CatalogueAppsArchiveCreateProductHaIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_4 = (
                        ApiV1CatalogueAppsArchiveCreateMaintainerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_5 = (
                        ApiV1CatalogueAppsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_6 = (
                        ApiV1CatalogueAppsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_7 = (
                        ApiV1CatalogueAppsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_8 = (
                        ApiV1CatalogueAppsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_9 = (
                        ApiV1CatalogueAppsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_10 = (
                        ApiV1CatalogueAppsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_11 = (
                        ApiV1CatalogueAppsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_12 = (
                        ApiV1CatalogueAppsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_13 = (
                        ApiV1CatalogueAppsArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_14 = (
                        ApiV1CatalogueAppsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_15 = (
                        ApiV1CatalogueAppsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_16 = (
                        ApiV1CatalogueAppsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_17 = (
                        ApiV1CatalogueAppsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_18 = (
                        ApiV1CatalogueAppsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_19 = (
                        ApiV1CatalogueAppsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_20 = (
                        ApiV1CatalogueAppsArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_21 = (
                        ApiV1CatalogueAppsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_22 = (
                        ApiV1CatalogueAppsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_23 = (
                        ApiV1CatalogueAppsArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_24 = (
                        ApiV1CatalogueAppsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_25 = (
                        ApiV1CatalogueAppsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_26 = (
                        ApiV1CatalogueAppsArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_27 = (
                        ApiV1CatalogueAppsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_28 = (
                        ApiV1CatalogueAppsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_29 = (
                        ApiV1CatalogueAppsArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_30 = (
                        ApiV1CatalogueAppsArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_31 = (
                        ApiV1CatalogueAppsArchiveCreateSerialNumberErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_32 = (
                        ApiV1CatalogueAppsArchiveCreateShortDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_33 = (
                        ApiV1CatalogueAppsArchiveCreateClaimErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_34 = (
                        ApiV1CatalogueAppsArchiveCreateDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_35 = (
                        ApiV1CatalogueAppsArchiveCreateIsNewErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_36 = (
                        ApiV1CatalogueAppsArchiveCreateScreenshotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_37 = (
                        ApiV1CatalogueAppsArchiveCreateMarkdownContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_38 = (
                        ApiV1CatalogueAppsArchiveCreateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_39 = (
                        ApiV1CatalogueAppsArchiveCreateHaEnabledExpressionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_40 = (
                        ApiV1CatalogueAppsArchiveCreateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_41 = (
                        ApiV1CatalogueAppsArchiveCreateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_42 = (
                        ApiV1CatalogueAppsArchiveCreateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_43 = (
                        ApiV1CatalogueAppsArchiveCreateTrackedAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_44 = (
                        ApiV1CatalogueAppsArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_45 = (
                        ApiV1CatalogueAppsArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_46 = (
                        ApiV1CatalogueAppsArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_47 = (
                        ApiV1CatalogueAppsArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_archive_create_error_type_48 = (
                        ApiV1CatalogueAppsArchiveCreateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_catalogue_apps_archive_create_error_type_49 = (
                    ApiV1CatalogueAppsArchiveCreateDependenciesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_catalogue_apps_archive_create_error_type_49

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_catalogue_apps_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_catalogue_apps_archive_create_validation_error.additional_properties = d
        return api_v1_catalogue_apps_archive_create_validation_error

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
