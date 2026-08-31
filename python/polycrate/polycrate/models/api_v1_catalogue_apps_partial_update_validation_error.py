from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_catalogue_apps_partial_update_annotations_error_component import (
        ApiV1CatalogueAppsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_archived_at_error_component import (
        ApiV1CatalogueAppsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_archived_by_error_component import (
        ApiV1CatalogueAppsPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_archived_error_component import (
        ApiV1CatalogueAppsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_archived_reason_error_component import (
        ApiV1CatalogueAppsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_artifact_package_error_component import (
        ApiV1CatalogueAppsPartialUpdateArtifactPackageErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_claim_error_component import (
        ApiV1CatalogueAppsPartialUpdateClaimErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_created_by_component_error_component import (
        ApiV1CatalogueAppsPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_created_by_user_error_component import (
        ApiV1CatalogueAppsPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_criticality_error_component import (
        ApiV1CatalogueAppsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_debug_mode_error_component import (
        ApiV1CatalogueAppsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_dependencies_error_component import (
        ApiV1CatalogueAppsPartialUpdateDependenciesErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_display_name_error_component import (
        ApiV1CatalogueAppsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_draft_error_component import (
        ApiV1CatalogueAppsPartialUpdateDraftErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_git_repository_url_error_component import (
        ApiV1CatalogueAppsPartialUpdateGitRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_ha_enabled_expression_error_component import (
        ApiV1CatalogueAppsPartialUpdateHaEnabledExpressionErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_is_new_error_component import (
        ApiV1CatalogueAppsPartialUpdateIsNewErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_kind_error_component import (
        ApiV1CatalogueAppsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_labels_error_component import (
        ApiV1CatalogueAppsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1CatalogueAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_managed_by_content_type_error_component import (
        ApiV1CatalogueAppsPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_managed_by_object_id_error_component import (
        ApiV1CatalogueAppsPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_markdown_content_error_component import (
        ApiV1CatalogueAppsPartialUpdateMarkdownContentErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_modified_by_user_error_component import (
        ApiV1CatalogueAppsPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_name_error_component import (
        ApiV1CatalogueAppsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_non_field_errors_error_component import (
        ApiV1CatalogueAppsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_platform_dns_record_created_error_component import (
        ApiV1CatalogueAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_platform_service_error_component import (
        ApiV1CatalogueAppsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_product_ha_id_error_component import (
        ApiV1CatalogueAppsPartialUpdateProductHaIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_product_regular_id_error_component import (
        ApiV1CatalogueAppsPartialUpdateProductRegularIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_provider_error_component import (
        ApiV1CatalogueAppsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_provider_id_error_component import (
        ApiV1CatalogueAppsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_provider_reference_error_component import (
        ApiV1CatalogueAppsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_reconciliation_enabled_error_component import (
        ApiV1CatalogueAppsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_registry_url_error_component import (
        ApiV1CatalogueAppsPartialUpdateRegistryUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_releases_url_error_component import (
        ApiV1CatalogueAppsPartialUpdateReleasesUrlErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_screenshot_error_component import (
        ApiV1CatalogueAppsPartialUpdateScreenshotErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_serial_number_error_component import (
        ApiV1CatalogueAppsPartialUpdateSerialNumberErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_short_description_error_component import (
        ApiV1CatalogueAppsPartialUpdateShortDescriptionErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_sla_availability_error_component import (
        ApiV1CatalogueAppsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_sla_target_error_component import (
        ApiV1CatalogueAppsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_sla_window_days_error_component import (
        ApiV1CatalogueAppsPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_slo_availability_error_component import (
        ApiV1CatalogueAppsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_slo_target_error_component import (
        ApiV1CatalogueAppsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_slo_window_days_error_component import (
        ApiV1CatalogueAppsPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_supports_ha_error_component import (
        ApiV1CatalogueAppsPartialUpdateSupportsHaErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_target_availability_error_component import (
        ApiV1CatalogueAppsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_tolerations_error_component import (
        ApiV1CatalogueAppsPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_catalogue_apps_partial_update_tracked_app_version_error_component import (
        ApiV1CatalogueAppsPartialUpdateTrackedAppVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CatalogueAppsPartialUpdateValidationError")


@_attrs_define
class ApiV1CatalogueAppsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CatalogueAppsPartialUpdateAnnotationsErrorComponent |
            ApiV1CatalogueAppsPartialUpdateArchivedAtErrorComponent |
            ApiV1CatalogueAppsPartialUpdateArchivedByErrorComponent | ApiV1CatalogueAppsPartialUpdateArchivedErrorComponent
            | ApiV1CatalogueAppsPartialUpdateArchivedReasonErrorComponent |
            ApiV1CatalogueAppsPartialUpdateArtifactPackageErrorComponent |
            ApiV1CatalogueAppsPartialUpdateClaimErrorComponent |
            ApiV1CatalogueAppsPartialUpdateCreatedByComponentErrorComponent |
            ApiV1CatalogueAppsPartialUpdateCreatedByUserErrorComponent |
            ApiV1CatalogueAppsPartialUpdateCriticalityErrorComponent |
            ApiV1CatalogueAppsPartialUpdateDebugModeErrorComponent |
            ApiV1CatalogueAppsPartialUpdateDependenciesErrorComponent |
            ApiV1CatalogueAppsPartialUpdateDisplayNameErrorComponent | ApiV1CatalogueAppsPartialUpdateDraftErrorComponent |
            ApiV1CatalogueAppsPartialUpdateGitRepositoryUrlErrorComponent |
            ApiV1CatalogueAppsPartialUpdateHaEnabledExpressionErrorComponent |
            ApiV1CatalogueAppsPartialUpdateIsNewErrorComponent | ApiV1CatalogueAppsPartialUpdateKindErrorComponent |
            ApiV1CatalogueAppsPartialUpdateLabelsErrorComponent |
            ApiV1CatalogueAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1CatalogueAppsPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1CatalogueAppsPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1CatalogueAppsPartialUpdateMarkdownContentErrorComponent |
            ApiV1CatalogueAppsPartialUpdateModifiedByUserErrorComponent | ApiV1CatalogueAppsPartialUpdateNameErrorComponent
            | ApiV1CatalogueAppsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1CatalogueAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1CatalogueAppsPartialUpdatePlatformServiceErrorComponent |
            ApiV1CatalogueAppsPartialUpdateProductHaIdErrorComponent |
            ApiV1CatalogueAppsPartialUpdateProductRegularIdErrorComponent |
            ApiV1CatalogueAppsPartialUpdateProviderErrorComponent | ApiV1CatalogueAppsPartialUpdateProviderIdErrorComponent
            | ApiV1CatalogueAppsPartialUpdateProviderReferenceErrorComponent |
            ApiV1CatalogueAppsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1CatalogueAppsPartialUpdateRegistryUrlErrorComponent |
            ApiV1CatalogueAppsPartialUpdateReleasesUrlErrorComponent |
            ApiV1CatalogueAppsPartialUpdateScreenshotErrorComponent |
            ApiV1CatalogueAppsPartialUpdateSerialNumberErrorComponent |
            ApiV1CatalogueAppsPartialUpdateShortDescriptionErrorComponent |
            ApiV1CatalogueAppsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1CatalogueAppsPartialUpdateSlaTargetErrorComponent |
            ApiV1CatalogueAppsPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1CatalogueAppsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1CatalogueAppsPartialUpdateSloTargetErrorComponent |
            ApiV1CatalogueAppsPartialUpdateSloWindowDaysErrorComponent |
            ApiV1CatalogueAppsPartialUpdateSupportsHaErrorComponent |
            ApiV1CatalogueAppsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1CatalogueAppsPartialUpdateTolerationsErrorComponent |
            ApiV1CatalogueAppsPartialUpdateTrackedAppVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CatalogueAppsPartialUpdateAnnotationsErrorComponent
        | ApiV1CatalogueAppsPartialUpdateArchivedAtErrorComponent
        | ApiV1CatalogueAppsPartialUpdateArchivedByErrorComponent
        | ApiV1CatalogueAppsPartialUpdateArchivedErrorComponent
        | ApiV1CatalogueAppsPartialUpdateArchivedReasonErrorComponent
        | ApiV1CatalogueAppsPartialUpdateArtifactPackageErrorComponent
        | ApiV1CatalogueAppsPartialUpdateClaimErrorComponent
        | ApiV1CatalogueAppsPartialUpdateCreatedByComponentErrorComponent
        | ApiV1CatalogueAppsPartialUpdateCreatedByUserErrorComponent
        | ApiV1CatalogueAppsPartialUpdateCriticalityErrorComponent
        | ApiV1CatalogueAppsPartialUpdateDebugModeErrorComponent
        | ApiV1CatalogueAppsPartialUpdateDependenciesErrorComponent
        | ApiV1CatalogueAppsPartialUpdateDisplayNameErrorComponent
        | ApiV1CatalogueAppsPartialUpdateDraftErrorComponent
        | ApiV1CatalogueAppsPartialUpdateGitRepositoryUrlErrorComponent
        | ApiV1CatalogueAppsPartialUpdateHaEnabledExpressionErrorComponent
        | ApiV1CatalogueAppsPartialUpdateIsNewErrorComponent
        | ApiV1CatalogueAppsPartialUpdateKindErrorComponent
        | ApiV1CatalogueAppsPartialUpdateLabelsErrorComponent
        | ApiV1CatalogueAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1CatalogueAppsPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1CatalogueAppsPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1CatalogueAppsPartialUpdateMarkdownContentErrorComponent
        | ApiV1CatalogueAppsPartialUpdateModifiedByUserErrorComponent
        | ApiV1CatalogueAppsPartialUpdateNameErrorComponent
        | ApiV1CatalogueAppsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1CatalogueAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1CatalogueAppsPartialUpdatePlatformServiceErrorComponent
        | ApiV1CatalogueAppsPartialUpdateProductHaIdErrorComponent
        | ApiV1CatalogueAppsPartialUpdateProductRegularIdErrorComponent
        | ApiV1CatalogueAppsPartialUpdateProviderErrorComponent
        | ApiV1CatalogueAppsPartialUpdateProviderIdErrorComponent
        | ApiV1CatalogueAppsPartialUpdateProviderReferenceErrorComponent
        | ApiV1CatalogueAppsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1CatalogueAppsPartialUpdateRegistryUrlErrorComponent
        | ApiV1CatalogueAppsPartialUpdateReleasesUrlErrorComponent
        | ApiV1CatalogueAppsPartialUpdateScreenshotErrorComponent
        | ApiV1CatalogueAppsPartialUpdateSerialNumberErrorComponent
        | ApiV1CatalogueAppsPartialUpdateShortDescriptionErrorComponent
        | ApiV1CatalogueAppsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1CatalogueAppsPartialUpdateSlaTargetErrorComponent
        | ApiV1CatalogueAppsPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1CatalogueAppsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1CatalogueAppsPartialUpdateSloTargetErrorComponent
        | ApiV1CatalogueAppsPartialUpdateSloWindowDaysErrorComponent
        | ApiV1CatalogueAppsPartialUpdateSupportsHaErrorComponent
        | ApiV1CatalogueAppsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1CatalogueAppsPartialUpdateTolerationsErrorComponent
        | ApiV1CatalogueAppsPartialUpdateTrackedAppVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_catalogue_apps_partial_update_annotations_error_component import (
            ApiV1CatalogueAppsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_archived_at_error_component import (
            ApiV1CatalogueAppsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_archived_by_error_component import (
            ApiV1CatalogueAppsPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_archived_error_component import (
            ApiV1CatalogueAppsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_archived_reason_error_component import (
            ApiV1CatalogueAppsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_artifact_package_error_component import (
            ApiV1CatalogueAppsPartialUpdateArtifactPackageErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_claim_error_component import (
            ApiV1CatalogueAppsPartialUpdateClaimErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_created_by_component_error_component import (
            ApiV1CatalogueAppsPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_created_by_user_error_component import (
            ApiV1CatalogueAppsPartialUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_criticality_error_component import (
            ApiV1CatalogueAppsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_debug_mode_error_component import (
            ApiV1CatalogueAppsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_display_name_error_component import (
            ApiV1CatalogueAppsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_draft_error_component import (
            ApiV1CatalogueAppsPartialUpdateDraftErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_git_repository_url_error_component import (
            ApiV1CatalogueAppsPartialUpdateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_ha_enabled_expression_error_component import (
            ApiV1CatalogueAppsPartialUpdateHaEnabledExpressionErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_is_new_error_component import (
            ApiV1CatalogueAppsPartialUpdateIsNewErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_kind_error_component import (
            ApiV1CatalogueAppsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_labels_error_component import (
            ApiV1CatalogueAppsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1CatalogueAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_managed_by_content_type_error_component import (
            ApiV1CatalogueAppsPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_managed_by_object_id_error_component import (
            ApiV1CatalogueAppsPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_markdown_content_error_component import (
            ApiV1CatalogueAppsPartialUpdateMarkdownContentErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_modified_by_user_error_component import (
            ApiV1CatalogueAppsPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_name_error_component import (
            ApiV1CatalogueAppsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_non_field_errors_error_component import (
            ApiV1CatalogueAppsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_platform_dns_record_created_error_component import (
            ApiV1CatalogueAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_platform_service_error_component import (
            ApiV1CatalogueAppsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_product_ha_id_error_component import (
            ApiV1CatalogueAppsPartialUpdateProductHaIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_product_regular_id_error_component import (
            ApiV1CatalogueAppsPartialUpdateProductRegularIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_provider_error_component import (
            ApiV1CatalogueAppsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_provider_id_error_component import (
            ApiV1CatalogueAppsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_provider_reference_error_component import (
            ApiV1CatalogueAppsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_reconciliation_enabled_error_component import (
            ApiV1CatalogueAppsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_registry_url_error_component import (
            ApiV1CatalogueAppsPartialUpdateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_releases_url_error_component import (
            ApiV1CatalogueAppsPartialUpdateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_screenshot_error_component import (
            ApiV1CatalogueAppsPartialUpdateScreenshotErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_serial_number_error_component import (
            ApiV1CatalogueAppsPartialUpdateSerialNumberErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_short_description_error_component import (
            ApiV1CatalogueAppsPartialUpdateShortDescriptionErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_sla_availability_error_component import (
            ApiV1CatalogueAppsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_sla_target_error_component import (
            ApiV1CatalogueAppsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_sla_window_days_error_component import (
            ApiV1CatalogueAppsPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_slo_availability_error_component import (
            ApiV1CatalogueAppsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_slo_target_error_component import (
            ApiV1CatalogueAppsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_slo_window_days_error_component import (
            ApiV1CatalogueAppsPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_supports_ha_error_component import (
            ApiV1CatalogueAppsPartialUpdateSupportsHaErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_target_availability_error_component import (
            ApiV1CatalogueAppsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_tolerations_error_component import (
            ApiV1CatalogueAppsPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_tracked_app_version_error_component import (
            ApiV1CatalogueAppsPartialUpdateTrackedAppVersionErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateProductRegularIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateProductHaIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1CatalogueAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateSerialNumberErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateShortDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateClaimErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateIsNewErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateScreenshotErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateMarkdownContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateSupportsHaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateHaEnabledExpressionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateRegistryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateReleasesUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateGitRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateTrackedAppVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CatalogueAppsPartialUpdateArtifactPackageErrorComponent):
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
        from ..models.api_v1_catalogue_apps_partial_update_annotations_error_component import (
            ApiV1CatalogueAppsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_archived_at_error_component import (
            ApiV1CatalogueAppsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_archived_by_error_component import (
            ApiV1CatalogueAppsPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_archived_error_component import (
            ApiV1CatalogueAppsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_archived_reason_error_component import (
            ApiV1CatalogueAppsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_artifact_package_error_component import (
            ApiV1CatalogueAppsPartialUpdateArtifactPackageErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_claim_error_component import (
            ApiV1CatalogueAppsPartialUpdateClaimErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_created_by_component_error_component import (
            ApiV1CatalogueAppsPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_created_by_user_error_component import (
            ApiV1CatalogueAppsPartialUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_criticality_error_component import (
            ApiV1CatalogueAppsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_debug_mode_error_component import (
            ApiV1CatalogueAppsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_dependencies_error_component import (
            ApiV1CatalogueAppsPartialUpdateDependenciesErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_display_name_error_component import (
            ApiV1CatalogueAppsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_draft_error_component import (
            ApiV1CatalogueAppsPartialUpdateDraftErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_git_repository_url_error_component import (
            ApiV1CatalogueAppsPartialUpdateGitRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_ha_enabled_expression_error_component import (
            ApiV1CatalogueAppsPartialUpdateHaEnabledExpressionErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_is_new_error_component import (
            ApiV1CatalogueAppsPartialUpdateIsNewErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_kind_error_component import (
            ApiV1CatalogueAppsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_labels_error_component import (
            ApiV1CatalogueAppsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1CatalogueAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_managed_by_content_type_error_component import (
            ApiV1CatalogueAppsPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_managed_by_object_id_error_component import (
            ApiV1CatalogueAppsPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_markdown_content_error_component import (
            ApiV1CatalogueAppsPartialUpdateMarkdownContentErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_modified_by_user_error_component import (
            ApiV1CatalogueAppsPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_name_error_component import (
            ApiV1CatalogueAppsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_non_field_errors_error_component import (
            ApiV1CatalogueAppsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_platform_dns_record_created_error_component import (
            ApiV1CatalogueAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_platform_service_error_component import (
            ApiV1CatalogueAppsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_product_ha_id_error_component import (
            ApiV1CatalogueAppsPartialUpdateProductHaIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_product_regular_id_error_component import (
            ApiV1CatalogueAppsPartialUpdateProductRegularIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_provider_error_component import (
            ApiV1CatalogueAppsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_provider_id_error_component import (
            ApiV1CatalogueAppsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_provider_reference_error_component import (
            ApiV1CatalogueAppsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_reconciliation_enabled_error_component import (
            ApiV1CatalogueAppsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_registry_url_error_component import (
            ApiV1CatalogueAppsPartialUpdateRegistryUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_releases_url_error_component import (
            ApiV1CatalogueAppsPartialUpdateReleasesUrlErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_screenshot_error_component import (
            ApiV1CatalogueAppsPartialUpdateScreenshotErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_serial_number_error_component import (
            ApiV1CatalogueAppsPartialUpdateSerialNumberErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_short_description_error_component import (
            ApiV1CatalogueAppsPartialUpdateShortDescriptionErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_sla_availability_error_component import (
            ApiV1CatalogueAppsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_sla_target_error_component import (
            ApiV1CatalogueAppsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_sla_window_days_error_component import (
            ApiV1CatalogueAppsPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_slo_availability_error_component import (
            ApiV1CatalogueAppsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_slo_target_error_component import (
            ApiV1CatalogueAppsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_slo_window_days_error_component import (
            ApiV1CatalogueAppsPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_supports_ha_error_component import (
            ApiV1CatalogueAppsPartialUpdateSupportsHaErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_target_availability_error_component import (
            ApiV1CatalogueAppsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_tolerations_error_component import (
            ApiV1CatalogueAppsPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_catalogue_apps_partial_update_tracked_app_version_error_component import (
            ApiV1CatalogueAppsPartialUpdateTrackedAppVersionErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CatalogueAppsPartialUpdateAnnotationsErrorComponent
                | ApiV1CatalogueAppsPartialUpdateArchivedAtErrorComponent
                | ApiV1CatalogueAppsPartialUpdateArchivedByErrorComponent
                | ApiV1CatalogueAppsPartialUpdateArchivedErrorComponent
                | ApiV1CatalogueAppsPartialUpdateArchivedReasonErrorComponent
                | ApiV1CatalogueAppsPartialUpdateArtifactPackageErrorComponent
                | ApiV1CatalogueAppsPartialUpdateClaimErrorComponent
                | ApiV1CatalogueAppsPartialUpdateCreatedByComponentErrorComponent
                | ApiV1CatalogueAppsPartialUpdateCreatedByUserErrorComponent
                | ApiV1CatalogueAppsPartialUpdateCriticalityErrorComponent
                | ApiV1CatalogueAppsPartialUpdateDebugModeErrorComponent
                | ApiV1CatalogueAppsPartialUpdateDependenciesErrorComponent
                | ApiV1CatalogueAppsPartialUpdateDisplayNameErrorComponent
                | ApiV1CatalogueAppsPartialUpdateDraftErrorComponent
                | ApiV1CatalogueAppsPartialUpdateGitRepositoryUrlErrorComponent
                | ApiV1CatalogueAppsPartialUpdateHaEnabledExpressionErrorComponent
                | ApiV1CatalogueAppsPartialUpdateIsNewErrorComponent
                | ApiV1CatalogueAppsPartialUpdateKindErrorComponent
                | ApiV1CatalogueAppsPartialUpdateLabelsErrorComponent
                | ApiV1CatalogueAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1CatalogueAppsPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1CatalogueAppsPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1CatalogueAppsPartialUpdateMarkdownContentErrorComponent
                | ApiV1CatalogueAppsPartialUpdateModifiedByUserErrorComponent
                | ApiV1CatalogueAppsPartialUpdateNameErrorComponent
                | ApiV1CatalogueAppsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1CatalogueAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1CatalogueAppsPartialUpdatePlatformServiceErrorComponent
                | ApiV1CatalogueAppsPartialUpdateProductHaIdErrorComponent
                | ApiV1CatalogueAppsPartialUpdateProductRegularIdErrorComponent
                | ApiV1CatalogueAppsPartialUpdateProviderErrorComponent
                | ApiV1CatalogueAppsPartialUpdateProviderIdErrorComponent
                | ApiV1CatalogueAppsPartialUpdateProviderReferenceErrorComponent
                | ApiV1CatalogueAppsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1CatalogueAppsPartialUpdateRegistryUrlErrorComponent
                | ApiV1CatalogueAppsPartialUpdateReleasesUrlErrorComponent
                | ApiV1CatalogueAppsPartialUpdateScreenshotErrorComponent
                | ApiV1CatalogueAppsPartialUpdateSerialNumberErrorComponent
                | ApiV1CatalogueAppsPartialUpdateShortDescriptionErrorComponent
                | ApiV1CatalogueAppsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1CatalogueAppsPartialUpdateSlaTargetErrorComponent
                | ApiV1CatalogueAppsPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1CatalogueAppsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1CatalogueAppsPartialUpdateSloTargetErrorComponent
                | ApiV1CatalogueAppsPartialUpdateSloWindowDaysErrorComponent
                | ApiV1CatalogueAppsPartialUpdateSupportsHaErrorComponent
                | ApiV1CatalogueAppsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1CatalogueAppsPartialUpdateTolerationsErrorComponent
                | ApiV1CatalogueAppsPartialUpdateTrackedAppVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_0 = (
                        ApiV1CatalogueAppsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_1 = (
                        ApiV1CatalogueAppsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_2 = (
                        ApiV1CatalogueAppsPartialUpdateProductRegularIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_3 = (
                        ApiV1CatalogueAppsPartialUpdateProductHaIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_4 = (
                        ApiV1CatalogueAppsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_5 = (
                        ApiV1CatalogueAppsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_6 = (
                        ApiV1CatalogueAppsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_7 = (
                        ApiV1CatalogueAppsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_8 = (
                        ApiV1CatalogueAppsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_9 = (
                        ApiV1CatalogueAppsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_10 = (
                        ApiV1CatalogueAppsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_11 = (
                        ApiV1CatalogueAppsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_12 = (
                        ApiV1CatalogueAppsPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_13 = (
                        ApiV1CatalogueAppsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_14 = (
                        ApiV1CatalogueAppsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_15 = (
                        ApiV1CatalogueAppsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_16 = (
                        ApiV1CatalogueAppsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_17 = (
                        ApiV1CatalogueAppsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_18 = (
                        ApiV1CatalogueAppsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_19 = (
                        ApiV1CatalogueAppsPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_20 = (
                        ApiV1CatalogueAppsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_21 = (
                        ApiV1CatalogueAppsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_22 = (
                        ApiV1CatalogueAppsPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_23 = (
                        ApiV1CatalogueAppsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_24 = (
                        ApiV1CatalogueAppsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_25 = (
                        ApiV1CatalogueAppsPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_26 = (
                        ApiV1CatalogueAppsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_27 = (
                        ApiV1CatalogueAppsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_28 = (
                        ApiV1CatalogueAppsPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_29 = (
                        ApiV1CatalogueAppsPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_30 = (
                        ApiV1CatalogueAppsPartialUpdateSerialNumberErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_31 = (
                        ApiV1CatalogueAppsPartialUpdateShortDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_32 = (
                        ApiV1CatalogueAppsPartialUpdateClaimErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_33 = (
                        ApiV1CatalogueAppsPartialUpdateDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_34 = (
                        ApiV1CatalogueAppsPartialUpdateIsNewErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_35 = (
                        ApiV1CatalogueAppsPartialUpdateScreenshotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_36 = (
                        ApiV1CatalogueAppsPartialUpdateMarkdownContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_37 = (
                        ApiV1CatalogueAppsPartialUpdateSupportsHaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_38 = (
                        ApiV1CatalogueAppsPartialUpdateHaEnabledExpressionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_39 = (
                        ApiV1CatalogueAppsPartialUpdateRegistryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_40 = (
                        ApiV1CatalogueAppsPartialUpdateReleasesUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_41 = (
                        ApiV1CatalogueAppsPartialUpdateGitRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_42 = (
                        ApiV1CatalogueAppsPartialUpdateTrackedAppVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_43 = (
                        ApiV1CatalogueAppsPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_44 = (
                        ApiV1CatalogueAppsPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_45 = (
                        ApiV1CatalogueAppsPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_46 = (
                        ApiV1CatalogueAppsPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_catalogue_apps_partial_update_error_type_47 = (
                        ApiV1CatalogueAppsPartialUpdateArtifactPackageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_catalogue_apps_partial_update_error_type_48 = (
                    ApiV1CatalogueAppsPartialUpdateDependenciesErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_catalogue_apps_partial_update_error_type_48

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_catalogue_apps_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_catalogue_apps_partial_update_validation_error.additional_properties = d
        return api_v1_catalogue_apps_partial_update_validation_error

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
