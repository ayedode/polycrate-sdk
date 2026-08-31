from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_catalogue_apps_update_annotations_error_component import (
        ApiV1CatalogueAppsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_archived_at_error_component import (
        ApiV1CatalogueAppsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_archived_by_error_component import (
        ApiV1CatalogueAppsUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_archived_error_component import (
        ApiV1CatalogueAppsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_archived_reason_error_component import (
        ApiV1CatalogueAppsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_artifact_package_error_component import (
        ApiV1CatalogueAppsUpdateArtifactPackageErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_claim_error_component import ApiV1CatalogueAppsUpdateClaimErrorComponent
    from ..models.api_v1_catalogue_apps_update_created_by_component_error_component import (
        ApiV1CatalogueAppsUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_created_by_user_error_component import (
        ApiV1CatalogueAppsUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_criticality_error_component import (
        ApiV1CatalogueAppsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_debug_mode_error_component import (
        ApiV1CatalogueAppsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_dependencies_error_component import (
        ApiV1CatalogueAppsUpdateDependenciesErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_display_name_error_component import (
        ApiV1CatalogueAppsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_draft_error_component import ApiV1CatalogueAppsUpdateDraftErrorComponent
    from ..models.api_v1_catalogue_apps_update_git_repository_url_error_component import (
        ApiV1CatalogueAppsUpdateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_ha_enabled_expression_error_component import (
        ApiV1CatalogueAppsUpdateHaEnabledExpressionErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_is_new_error_component import ApiV1CatalogueAppsUpdateIsNewErrorComponent
    from ..models.api_v1_catalogue_apps_update_kind_error_component import ApiV1CatalogueAppsUpdateKindErrorComponent
    from ..models.api_v1_catalogue_apps_update_labels_error_component import (
        ApiV1CatalogueAppsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1CatalogueAppsUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_managed_by_content_type_error_component import (
        ApiV1CatalogueAppsUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_managed_by_object_id_error_component import (
        ApiV1CatalogueAppsUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_markdown_content_error_component import (
        ApiV1CatalogueAppsUpdateMarkdownContentErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_modified_by_user_error_component import (
        ApiV1CatalogueAppsUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_name_error_component import ApiV1CatalogueAppsUpdateNameErrorComponent
    from ..models.api_v1_catalogue_apps_update_non_field_errors_error_component import (
        ApiV1CatalogueAppsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_platform_dns_record_created_error_component import (
        ApiV1CatalogueAppsUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_platform_service_error_component import (
        ApiV1CatalogueAppsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_product_ha_id_error_component import (
        ApiV1CatalogueAppsUpdateProductHaIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_product_regular_id_error_component import (
        ApiV1CatalogueAppsUpdateProductRegularIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_provider_error_component import (
        ApiV1CatalogueAppsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_provider_id_error_component import (
        ApiV1CatalogueAppsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_provider_reference_error_component import (
        ApiV1CatalogueAppsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_reconciliation_enabled_error_component import (
        ApiV1CatalogueAppsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_registry_url_error_component import (
        ApiV1CatalogueAppsUpdateRegistryUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_releases_url_error_component import (
        ApiV1CatalogueAppsUpdateReleasesUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_screenshot_error_component import (
        ApiV1CatalogueAppsUpdateScreenshotErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_serial_number_error_component import (
        ApiV1CatalogueAppsUpdateSerialNumberErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_short_description_error_component import (
        ApiV1CatalogueAppsUpdateShortDescriptionErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_sla_availability_error_component import (
        ApiV1CatalogueAppsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_sla_target_error_component import (
        ApiV1CatalogueAppsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_sla_window_days_error_component import (
        ApiV1CatalogueAppsUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_slo_availability_error_component import (
        ApiV1CatalogueAppsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_slo_target_error_component import (
        ApiV1CatalogueAppsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_slo_window_days_error_component import (
        ApiV1CatalogueAppsUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_supports_ha_error_component import (
        ApiV1CatalogueAppsUpdateSupportsHaErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_target_availability_error_component import (
        ApiV1CatalogueAppsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_tolerations_error_component import (
        ApiV1CatalogueAppsUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_update_tracked_app_version_error_component import (
        ApiV1CatalogueAppsUpdateTrackedAppVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CatalogueAppsUpdateValidationError")


@_attrs_define
class ApiV1CatalogueAppsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CatalogueAppsUpdateAnnotationsErrorComponent |
            ApiV1CatalogueAppsUpdateArchivedAtErrorComponent | ApiV1CatalogueAppsUpdateArchivedByErrorComponent |
            ApiV1CatalogueAppsUpdateArchivedErrorComponent | ApiV1CatalogueAppsUpdateArchivedReasonErrorComponent |
            ApiV1CatalogueAppsUpdateArtifactPackageErrorComponent | ApiV1CatalogueAppsUpdateClaimErrorComponent |
            ApiV1CatalogueAppsUpdateCreatedByComponentErrorComponent | ApiV1CatalogueAppsUpdateCreatedByUserErrorComponent |
            ApiV1CatalogueAppsUpdateCriticalityErrorComponent | ApiV1CatalogueAppsUpdateDebugModeErrorComponent |
            ApiV1CatalogueAppsUpdateDependenciesErrorComponent | ApiV1CatalogueAppsUpdateDisplayNameErrorComponent |
            ApiV1CatalogueAppsUpdateDraftErrorComponent | ApiV1CatalogueAppsUpdateGitRepositoryUrlErrorComponent |
            ApiV1CatalogueAppsUpdateHaEnabledExpressionErrorComponent | ApiV1CatalogueAppsUpdateIsNewErrorComponent |
            ApiV1CatalogueAppsUpdateKindErrorComponent | ApiV1CatalogueAppsUpdateLabelsErrorComponent |
            ApiV1CatalogueAppsUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1CatalogueAppsUpdateManagedByContentTypeErrorComponent |
            ApiV1CatalogueAppsUpdateManagedByObjectIdErrorComponent | ApiV1CatalogueAppsUpdateMarkdownContentErrorComponent
            | ApiV1CatalogueAppsUpdateModifiedByUserErrorComponent | ApiV1CatalogueAppsUpdateNameErrorComponent |
            ApiV1CatalogueAppsUpdateNonFieldErrorsErrorComponent |
            ApiV1CatalogueAppsUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1CatalogueAppsUpdatePlatformServiceErrorComponent | ApiV1CatalogueAppsUpdateProductHaIdErrorComponent |
            ApiV1CatalogueAppsUpdateProductRegularIdErrorComponent | ApiV1CatalogueAppsUpdateProviderErrorComponent |
            ApiV1CatalogueAppsUpdateProviderIdErrorComponent | ApiV1CatalogueAppsUpdateProviderReferenceErrorComponent |
            ApiV1CatalogueAppsUpdateReconciliationEnabledErrorComponent | ApiV1CatalogueAppsUpdateRegistryUrlErrorComponent
            | ApiV1CatalogueAppsUpdateReleasesUrlErrorComponent | ApiV1CatalogueAppsUpdateScreenshotErrorComponent |
            ApiV1CatalogueAppsUpdateSerialNumberErrorComponent | ApiV1CatalogueAppsUpdateShortDescriptionErrorComponent |
            ApiV1CatalogueAppsUpdateSlaAvailabilityErrorComponent | ApiV1CatalogueAppsUpdateSlaTargetErrorComponent |
            ApiV1CatalogueAppsUpdateSlaWindowDaysErrorComponent | ApiV1CatalogueAppsUpdateSloAvailabilityErrorComponent |
            ApiV1CatalogueAppsUpdateSloTargetErrorComponent | ApiV1CatalogueAppsUpdateSloWindowDaysErrorComponent |
            ApiV1CatalogueAppsUpdateSupportsHaErrorComponent | ApiV1CatalogueAppsUpdateTargetAvailabilityErrorComponent |
            ApiV1CatalogueAppsUpdateTolerationsErrorComponent | ApiV1CatalogueAppsUpdateTrackedAppVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CatalogueAppsUpdateAnnotationsErrorComponent
        | ApiV1CatalogueAppsUpdateArchivedAtErrorComponent
        | ApiV1CatalogueAppsUpdateArchivedByErrorComponent
        | ApiV1CatalogueAppsUpdateArchivedErrorComponent
        | ApiV1CatalogueAppsUpdateArchivedReasonErrorComponent
        | ApiV1CatalogueAppsUpdateArtifactPackageErrorComponent
        | ApiV1CatalogueAppsUpdateClaimErrorComponent
        | ApiV1CatalogueAppsUpdateCreatedByComponentErrorComponent
        | ApiV1CatalogueAppsUpdateCreatedByUserErrorComponent
        | ApiV1CatalogueAppsUpdateCriticalityErrorComponent
        | ApiV1CatalogueAppsUpdateDebugModeErrorComponent
        | ApiV1CatalogueAppsUpdateDependenciesErrorComponent
        | ApiV1CatalogueAppsUpdateDisplayNameErrorComponent
        | ApiV1CatalogueAppsUpdateDraftErrorComponent
        | ApiV1CatalogueAppsUpdateGitRepositoryUrlErrorComponent
        | ApiV1CatalogueAppsUpdateHaEnabledExpressionErrorComponent
        | ApiV1CatalogueAppsUpdateIsNewErrorComponent
        | ApiV1CatalogueAppsUpdateKindErrorComponent
        | ApiV1CatalogueAppsUpdateLabelsErrorComponent
        | ApiV1CatalogueAppsUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1CatalogueAppsUpdateManagedByContentTypeErrorComponent
        | ApiV1CatalogueAppsUpdateManagedByObjectIdErrorComponent
        | ApiV1CatalogueAppsUpdateMarkdownContentErrorComponent
        | ApiV1CatalogueAppsUpdateModifiedByUserErrorComponent
        | ApiV1CatalogueAppsUpdateNameErrorComponent
        | ApiV1CatalogueAppsUpdateNonFieldErrorsErrorComponent
        | ApiV1CatalogueAppsUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1CatalogueAppsUpdatePlatformServiceErrorComponent
        | ApiV1CatalogueAppsUpdateProductHaIdErrorComponent
        | ApiV1CatalogueAppsUpdateProductRegularIdErrorComponent
        | ApiV1CatalogueAppsUpdateProviderErrorComponent
        | ApiV1CatalogueAppsUpdateProviderIdErrorComponent
        | ApiV1CatalogueAppsUpdateProviderReferenceErrorComponent
        | ApiV1CatalogueAppsUpdateReconciliationEnabledErrorComponent
        | ApiV1CatalogueAppsUpdateRegistryUrlErrorComponent
        | ApiV1CatalogueAppsUpdateReleasesUrlErrorComponent
        | ApiV1CatalogueAppsUpdateScreenshotErrorComponent
        | ApiV1CatalogueAppsUpdateSerialNumberErrorComponent
        | ApiV1CatalogueAppsUpdateShortDescriptionErrorComponent
        | ApiV1CatalogueAppsUpdateSlaAvailabilityErrorComponent
        | ApiV1CatalogueAppsUpdateSlaTargetErrorComponent
        | ApiV1CatalogueAppsUpdateSlaWindowDaysErrorComponent
        | ApiV1CatalogueAppsUpdateSloAvailabilityErrorComponent
        | ApiV1CatalogueAppsUpdateSloTargetErrorComponent
        | ApiV1CatalogueAppsUpdateSloWindowDaysErrorComponent
        | ApiV1CatalogueAppsUpdateSupportsHaErrorComponent
        | ApiV1CatalogueAppsUpdateTargetAvailabilityErrorComponent
        | ApiV1CatalogueAppsUpdateTolerationsErrorComponent
        | ApiV1CatalogueAppsUpdateTrackedAppVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_catalogue_apps_update_annotations_error_component import (
            ApiV1CatalogueAppsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_archived_at_error_component import (
            ApiV1CatalogueAppsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_archived_by_error_component import (
            ApiV1CatalogueAppsUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_archived_error_component import (
            ApiV1CatalogueAppsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_archived_reason_error_component import (
            ApiV1CatalogueAppsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_artifact_package_error_component import (
            ApiV1CatalogueAppsUpdateArtifactPackageErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_claim_error_component import (
            ApiV1CatalogueAppsUpdateClaimErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_created_by_component_error_component import (
            ApiV1CatalogueAppsUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_created_by_user_error_component import (
            ApiV1CatalogueAppsUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_criticality_error_component import (
            ApiV1CatalogueAppsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_debug_mode_error_component import (
            ApiV1CatalogueAppsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_display_name_error_component import (
            ApiV1CatalogueAppsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_draft_error_component import (
            ApiV1CatalogueAppsUpdateDraftErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_git_repository_url_error_component import (
            ApiV1CatalogueAppsUpdateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_ha_enabled_expression_error_component import (
            ApiV1CatalogueAppsUpdateHaEnabledExpressionErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_is_new_error_component import (
            ApiV1CatalogueAppsUpdateIsNewErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_kind_error_component import (
            ApiV1CatalogueAppsUpdateKindErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_labels_error_component import (
            ApiV1CatalogueAppsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1CatalogueAppsUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_managed_by_content_type_error_component import (
            ApiV1CatalogueAppsUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_managed_by_object_id_error_component import (
            ApiV1CatalogueAppsUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_markdown_content_error_component import (
            ApiV1CatalogueAppsUpdateMarkdownContentErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_modified_by_user_error_component import (
            ApiV1CatalogueAppsUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_name_error_component import (
            ApiV1CatalogueAppsUpdateNameErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_non_field_errors_error_component import (
            ApiV1CatalogueAppsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_platform_dns_record_created_error_component import (
            ApiV1CatalogueAppsUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_platform_service_error_component import (
            ApiV1CatalogueAppsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_product_ha_id_error_component import (
            ApiV1CatalogueAppsUpdateProductHaIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_product_regular_id_error_component import (
            ApiV1CatalogueAppsUpdateProductRegularIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_provider_error_component import (
            ApiV1CatalogueAppsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_provider_id_error_component import (
            ApiV1CatalogueAppsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_provider_reference_error_component import (
            ApiV1CatalogueAppsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_reconciliation_enabled_error_component import (
            ApiV1CatalogueAppsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_registry_url_error_component import (
            ApiV1CatalogueAppsUpdateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_releases_url_error_component import (
            ApiV1CatalogueAppsUpdateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_screenshot_error_component import (
            ApiV1CatalogueAppsUpdateScreenshotErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_serial_number_error_component import (
            ApiV1CatalogueAppsUpdateSerialNumberErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_short_description_error_component import (
            ApiV1CatalogueAppsUpdateShortDescriptionErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_sla_availability_error_component import (
            ApiV1CatalogueAppsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_sla_target_error_component import (
            ApiV1CatalogueAppsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_sla_window_days_error_component import (
            ApiV1CatalogueAppsUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_slo_availability_error_component import (
            ApiV1CatalogueAppsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_slo_target_error_component import (
            ApiV1CatalogueAppsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_slo_window_days_error_component import (
            ApiV1CatalogueAppsUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_supports_ha_error_component import (
            ApiV1CatalogueAppsUpdateSupportsHaErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_target_availability_error_component import (
            ApiV1CatalogueAppsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_tolerations_error_component import (
            ApiV1CatalogueAppsUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_tracked_app_version_error_component import (
            ApiV1CatalogueAppsUpdateTrackedAppVersionErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CatalogueAppsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateProductRegularIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateProductHaIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateSerialNumberErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateShortDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateClaimErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateIsNewErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateScreenshotErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateMarkdownContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateHaEnabledExpressionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateTrackedAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsUpdateArtifactPackageErrorComponent):
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
        from ..models.api_v1_catalogue_apps_update_annotations_error_component import (
            ApiV1CatalogueAppsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_archived_at_error_component import (
            ApiV1CatalogueAppsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_archived_by_error_component import (
            ApiV1CatalogueAppsUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_archived_error_component import (
            ApiV1CatalogueAppsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_archived_reason_error_component import (
            ApiV1CatalogueAppsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_artifact_package_error_component import (
            ApiV1CatalogueAppsUpdateArtifactPackageErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_claim_error_component import (
            ApiV1CatalogueAppsUpdateClaimErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_created_by_component_error_component import (
            ApiV1CatalogueAppsUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_created_by_user_error_component import (
            ApiV1CatalogueAppsUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_criticality_error_component import (
            ApiV1CatalogueAppsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_debug_mode_error_component import (
            ApiV1CatalogueAppsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_dependencies_error_component import (
            ApiV1CatalogueAppsUpdateDependenciesErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_display_name_error_component import (
            ApiV1CatalogueAppsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_draft_error_component import (
            ApiV1CatalogueAppsUpdateDraftErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_git_repository_url_error_component import (
            ApiV1CatalogueAppsUpdateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_ha_enabled_expression_error_component import (
            ApiV1CatalogueAppsUpdateHaEnabledExpressionErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_is_new_error_component import (
            ApiV1CatalogueAppsUpdateIsNewErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_kind_error_component import (
            ApiV1CatalogueAppsUpdateKindErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_labels_error_component import (
            ApiV1CatalogueAppsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1CatalogueAppsUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_managed_by_content_type_error_component import (
            ApiV1CatalogueAppsUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_managed_by_object_id_error_component import (
            ApiV1CatalogueAppsUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_markdown_content_error_component import (
            ApiV1CatalogueAppsUpdateMarkdownContentErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_modified_by_user_error_component import (
            ApiV1CatalogueAppsUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_name_error_component import (
            ApiV1CatalogueAppsUpdateNameErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_non_field_errors_error_component import (
            ApiV1CatalogueAppsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_platform_dns_record_created_error_component import (
            ApiV1CatalogueAppsUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_platform_service_error_component import (
            ApiV1CatalogueAppsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_product_ha_id_error_component import (
            ApiV1CatalogueAppsUpdateProductHaIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_product_regular_id_error_component import (
            ApiV1CatalogueAppsUpdateProductRegularIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_provider_error_component import (
            ApiV1CatalogueAppsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_provider_id_error_component import (
            ApiV1CatalogueAppsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_provider_reference_error_component import (
            ApiV1CatalogueAppsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_reconciliation_enabled_error_component import (
            ApiV1CatalogueAppsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_registry_url_error_component import (
            ApiV1CatalogueAppsUpdateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_releases_url_error_component import (
            ApiV1CatalogueAppsUpdateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_screenshot_error_component import (
            ApiV1CatalogueAppsUpdateScreenshotErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_serial_number_error_component import (
            ApiV1CatalogueAppsUpdateSerialNumberErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_short_description_error_component import (
            ApiV1CatalogueAppsUpdateShortDescriptionErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_sla_availability_error_component import (
            ApiV1CatalogueAppsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_sla_target_error_component import (
            ApiV1CatalogueAppsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_sla_window_days_error_component import (
            ApiV1CatalogueAppsUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_slo_availability_error_component import (
            ApiV1CatalogueAppsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_slo_target_error_component import (
            ApiV1CatalogueAppsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_slo_window_days_error_component import (
            ApiV1CatalogueAppsUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_supports_ha_error_component import (
            ApiV1CatalogueAppsUpdateSupportsHaErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_target_availability_error_component import (
            ApiV1CatalogueAppsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_tolerations_error_component import (
            ApiV1CatalogueAppsUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_update_tracked_app_version_error_component import (
            ApiV1CatalogueAppsUpdateTrackedAppVersionErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CatalogueAppsUpdateAnnotationsErrorComponent
                | ApiV1CatalogueAppsUpdateArchivedAtErrorComponent
                | ApiV1CatalogueAppsUpdateArchivedByErrorComponent
                | ApiV1CatalogueAppsUpdateArchivedErrorComponent
                | ApiV1CatalogueAppsUpdateArchivedReasonErrorComponent
                | ApiV1CatalogueAppsUpdateArtifactPackageErrorComponent
                | ApiV1CatalogueAppsUpdateClaimErrorComponent
                | ApiV1CatalogueAppsUpdateCreatedByComponentErrorComponent
                | ApiV1CatalogueAppsUpdateCreatedByUserErrorComponent
                | ApiV1CatalogueAppsUpdateCriticalityErrorComponent
                | ApiV1CatalogueAppsUpdateDebugModeErrorComponent
                | ApiV1CatalogueAppsUpdateDependenciesErrorComponent
                | ApiV1CatalogueAppsUpdateDisplayNameErrorComponent
                | ApiV1CatalogueAppsUpdateDraftErrorComponent
                | ApiV1CatalogueAppsUpdateGitRepositoryUrlErrorComponent
                | ApiV1CatalogueAppsUpdateHaEnabledExpressionErrorComponent
                | ApiV1CatalogueAppsUpdateIsNewErrorComponent
                | ApiV1CatalogueAppsUpdateKindErrorComponent
                | ApiV1CatalogueAppsUpdateLabelsErrorComponent
                | ApiV1CatalogueAppsUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1CatalogueAppsUpdateManagedByContentTypeErrorComponent
                | ApiV1CatalogueAppsUpdateManagedByObjectIdErrorComponent
                | ApiV1CatalogueAppsUpdateMarkdownContentErrorComponent
                | ApiV1CatalogueAppsUpdateModifiedByUserErrorComponent
                | ApiV1CatalogueAppsUpdateNameErrorComponent
                | ApiV1CatalogueAppsUpdateNonFieldErrorsErrorComponent
                | ApiV1CatalogueAppsUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1CatalogueAppsUpdatePlatformServiceErrorComponent
                | ApiV1CatalogueAppsUpdateProductHaIdErrorComponent
                | ApiV1CatalogueAppsUpdateProductRegularIdErrorComponent
                | ApiV1CatalogueAppsUpdateProviderErrorComponent
                | ApiV1CatalogueAppsUpdateProviderIdErrorComponent
                | ApiV1CatalogueAppsUpdateProviderReferenceErrorComponent
                | ApiV1CatalogueAppsUpdateReconciliationEnabledErrorComponent
                | ApiV1CatalogueAppsUpdateRegistryUrlErrorComponent
                | ApiV1CatalogueAppsUpdateReleasesUrlErrorComponent
                | ApiV1CatalogueAppsUpdateScreenshotErrorComponent
                | ApiV1CatalogueAppsUpdateSerialNumberErrorComponent
                | ApiV1CatalogueAppsUpdateShortDescriptionErrorComponent
                | ApiV1CatalogueAppsUpdateSlaAvailabilityErrorComponent
                | ApiV1CatalogueAppsUpdateSlaTargetErrorComponent
                | ApiV1CatalogueAppsUpdateSlaWindowDaysErrorComponent
                | ApiV1CatalogueAppsUpdateSloAvailabilityErrorComponent
                | ApiV1CatalogueAppsUpdateSloTargetErrorComponent
                | ApiV1CatalogueAppsUpdateSloWindowDaysErrorComponent
                | ApiV1CatalogueAppsUpdateSupportsHaErrorComponent
                | ApiV1CatalogueAppsUpdateTargetAvailabilityErrorComponent
                | ApiV1CatalogueAppsUpdateTolerationsErrorComponent
                | ApiV1CatalogueAppsUpdateTrackedAppVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_0 = (
                        ApiV1CatalogueAppsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_1 = (
                        ApiV1CatalogueAppsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_2 = (
                        ApiV1CatalogueAppsUpdateProductRegularIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_3 = (
                        ApiV1CatalogueAppsUpdateProductHaIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_4 = (
                        ApiV1CatalogueAppsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_5 = (
                        ApiV1CatalogueAppsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_6 = (
                        ApiV1CatalogueAppsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_7 = (
                        ApiV1CatalogueAppsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_8 = (
                        ApiV1CatalogueAppsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_9 = (
                        ApiV1CatalogueAppsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_10 = (
                        ApiV1CatalogueAppsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_11 = (
                        ApiV1CatalogueAppsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_12 = (
                        ApiV1CatalogueAppsUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_13 = (
                        ApiV1CatalogueAppsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_14 = (
                        ApiV1CatalogueAppsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_15 = (
                        ApiV1CatalogueAppsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_16 = (
                        ApiV1CatalogueAppsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_17 = (
                        ApiV1CatalogueAppsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_18 = (
                        ApiV1CatalogueAppsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_19 = (
                        ApiV1CatalogueAppsUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_20 = (
                        ApiV1CatalogueAppsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_21 = (
                        ApiV1CatalogueAppsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_22 = (
                        ApiV1CatalogueAppsUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_23 = (
                        ApiV1CatalogueAppsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_24 = (
                        ApiV1CatalogueAppsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_25 = (
                        ApiV1CatalogueAppsUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_26 = (
                        ApiV1CatalogueAppsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_27 = (
                        ApiV1CatalogueAppsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_28 = (
                        ApiV1CatalogueAppsUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_29 = (
                        ApiV1CatalogueAppsUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_30 = (
                        ApiV1CatalogueAppsUpdateSerialNumberErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_31 = (
                        ApiV1CatalogueAppsUpdateShortDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_32 = (
                        ApiV1CatalogueAppsUpdateClaimErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_33 = (
                        ApiV1CatalogueAppsUpdateDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_34 = (
                        ApiV1CatalogueAppsUpdateIsNewErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_35 = (
                        ApiV1CatalogueAppsUpdateScreenshotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_36 = (
                        ApiV1CatalogueAppsUpdateMarkdownContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_37 = (
                        ApiV1CatalogueAppsUpdateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_38 = (
                        ApiV1CatalogueAppsUpdateHaEnabledExpressionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_39 = (
                        ApiV1CatalogueAppsUpdateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_40 = (
                        ApiV1CatalogueAppsUpdateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_41 = (
                        ApiV1CatalogueAppsUpdateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_42 = (
                        ApiV1CatalogueAppsUpdateTrackedAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_43 = (
                        ApiV1CatalogueAppsUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_44 = (
                        ApiV1CatalogueAppsUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_45 = (
                        ApiV1CatalogueAppsUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_46 = (
                        ApiV1CatalogueAppsUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_update_error_type_47 = (
                        ApiV1CatalogueAppsUpdateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_catalogue_apps_update_error_type_48 = (
                    ApiV1CatalogueAppsUpdateDependenciesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_catalogue_apps_update_error_type_48

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_catalogue_apps_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_catalogue_apps_update_validation_error.additional_properties = d
        return api_v1_catalogue_apps_update_validation_error

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
