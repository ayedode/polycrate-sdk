from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alerts_partial_update_alert_router_error_component import (
        ApiV1AlertsPartialUpdateAlertRouterErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_annotations_error_component import (
        ApiV1AlertsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_archived_at_error_component import (
        ApiV1AlertsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_archived_error_component import (
        ApiV1AlertsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_archived_reason_error_component import (
        ApiV1AlertsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_block_error_component import ApiV1AlertsPartialUpdateBlockErrorComponent
    from ..models.api_v1_alerts_partial_update_category_error_component import (
        ApiV1AlertsPartialUpdateCategoryErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_criticality_error_component import (
        ApiV1AlertsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_dashboard_url_error_component import (
        ApiV1AlertsPartialUpdateDashboardUrlErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_debug_mode_error_component import (
        ApiV1AlertsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_display_name_error_component import (
        ApiV1AlertsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_external_url_error_component import (
        ApiV1AlertsPartialUpdateExternalUrlErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_fingerprint_error_component import (
        ApiV1AlertsPartialUpdateFingerprintErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_generator_url_error_component import (
        ApiV1AlertsPartialUpdateGeneratorUrlErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_k8s_app_error_component import (
        ApiV1AlertsPartialUpdateK8SAppErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_k8s_cluster_error_component import (
        ApiV1AlertsPartialUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_kind_error_component import ApiV1AlertsPartialUpdateKindErrorComponent
    from ..models.api_v1_alerts_partial_update_labels_error_component import (
        ApiV1AlertsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_last_seen_error_component import (
        ApiV1AlertsPartialUpdateLastSeenErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_message_error_component import (
        ApiV1AlertsPartialUpdateMessageErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_name_error_component import ApiV1AlertsPartialUpdateNameErrorComponent
    from ..models.api_v1_alerts_partial_update_namespace_error_component import (
        ApiV1AlertsPartialUpdateNamespaceErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_non_field_errors_error_component import (
        ApiV1AlertsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_panel_url_error_component import (
        ApiV1AlertsPartialUpdatePanelUrlErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_platform_service_error_component import (
        ApiV1AlertsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_pod_error_component import ApiV1AlertsPartialUpdatePodErrorComponent
    from ..models.api_v1_alerts_partial_update_provider_error_component import (
        ApiV1AlertsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_provider_id_error_component import (
        ApiV1AlertsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_provider_reference_error_component import (
        ApiV1AlertsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_reconciliation_enabled_error_component import (
        ApiV1AlertsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_silence_ends_at_error_component import (
        ApiV1AlertsPartialUpdateSilenceEndsAtErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_silence_url_error_component import (
        ApiV1AlertsPartialUpdateSilenceUrlErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_sla_availability_error_component import (
        ApiV1AlertsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_sla_target_error_component import (
        ApiV1AlertsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_slo_availability_error_component import (
        ApiV1AlertsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_slo_target_error_component import (
        ApiV1AlertsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_status_error_component import (
        ApiV1AlertsPartialUpdateStatusErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_suppressed_error_component import (
        ApiV1AlertsPartialUpdateSuppressedErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_target_availability_error_component import (
        ApiV1AlertsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_partial_update_title_error_component import ApiV1AlertsPartialUpdateTitleErrorComponent
    from ..models.api_v1_alerts_partial_update_tolerations_error_component import (
        ApiV1AlertsPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AlertsPartialUpdateValidationError")


@_attrs_define
class ApiV1AlertsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertsPartialUpdateAlertRouterErrorComponent |
            ApiV1AlertsPartialUpdateAnnotationsErrorComponent | ApiV1AlertsPartialUpdateArchivedAtErrorComponent |
            ApiV1AlertsPartialUpdateArchivedErrorComponent | ApiV1AlertsPartialUpdateArchivedReasonErrorComponent |
            ApiV1AlertsPartialUpdateBlockErrorComponent | ApiV1AlertsPartialUpdateCategoryErrorComponent |
            ApiV1AlertsPartialUpdateCriticalityErrorComponent | ApiV1AlertsPartialUpdateDashboardUrlErrorComponent |
            ApiV1AlertsPartialUpdateDebugModeErrorComponent | ApiV1AlertsPartialUpdateDisplayNameErrorComponent |
            ApiV1AlertsPartialUpdateExternalUrlErrorComponent | ApiV1AlertsPartialUpdateFingerprintErrorComponent |
            ApiV1AlertsPartialUpdateGeneratorUrlErrorComponent | ApiV1AlertsPartialUpdateK8SAppErrorComponent |
            ApiV1AlertsPartialUpdateK8SClusterErrorComponent | ApiV1AlertsPartialUpdateKindErrorComponent |
            ApiV1AlertsPartialUpdateLabelsErrorComponent | ApiV1AlertsPartialUpdateLastSeenErrorComponent |
            ApiV1AlertsPartialUpdateMessageErrorComponent | ApiV1AlertsPartialUpdateNameErrorComponent |
            ApiV1AlertsPartialUpdateNamespaceErrorComponent | ApiV1AlertsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1AlertsPartialUpdatePanelUrlErrorComponent | ApiV1AlertsPartialUpdatePlatformServiceErrorComponent |
            ApiV1AlertsPartialUpdatePodErrorComponent | ApiV1AlertsPartialUpdateProviderErrorComponent |
            ApiV1AlertsPartialUpdateProviderIdErrorComponent | ApiV1AlertsPartialUpdateProviderReferenceErrorComponent |
            ApiV1AlertsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1AlertsPartialUpdateSilenceEndsAtErrorComponent | ApiV1AlertsPartialUpdateSilenceUrlErrorComponent |
            ApiV1AlertsPartialUpdateSlaAvailabilityErrorComponent | ApiV1AlertsPartialUpdateSlaTargetErrorComponent |
            ApiV1AlertsPartialUpdateSloAvailabilityErrorComponent | ApiV1AlertsPartialUpdateSloTargetErrorComponent |
            ApiV1AlertsPartialUpdateStatusErrorComponent | ApiV1AlertsPartialUpdateSuppressedErrorComponent |
            ApiV1AlertsPartialUpdateTargetAvailabilityErrorComponent | ApiV1AlertsPartialUpdateTitleErrorComponent |
            ApiV1AlertsPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertsPartialUpdateAlertRouterErrorComponent
        | ApiV1AlertsPartialUpdateAnnotationsErrorComponent
        | ApiV1AlertsPartialUpdateArchivedAtErrorComponent
        | ApiV1AlertsPartialUpdateArchivedErrorComponent
        | ApiV1AlertsPartialUpdateArchivedReasonErrorComponent
        | ApiV1AlertsPartialUpdateBlockErrorComponent
        | ApiV1AlertsPartialUpdateCategoryErrorComponent
        | ApiV1AlertsPartialUpdateCriticalityErrorComponent
        | ApiV1AlertsPartialUpdateDashboardUrlErrorComponent
        | ApiV1AlertsPartialUpdateDebugModeErrorComponent
        | ApiV1AlertsPartialUpdateDisplayNameErrorComponent
        | ApiV1AlertsPartialUpdateExternalUrlErrorComponent
        | ApiV1AlertsPartialUpdateFingerprintErrorComponent
        | ApiV1AlertsPartialUpdateGeneratorUrlErrorComponent
        | ApiV1AlertsPartialUpdateK8SAppErrorComponent
        | ApiV1AlertsPartialUpdateK8SClusterErrorComponent
        | ApiV1AlertsPartialUpdateKindErrorComponent
        | ApiV1AlertsPartialUpdateLabelsErrorComponent
        | ApiV1AlertsPartialUpdateLastSeenErrorComponent
        | ApiV1AlertsPartialUpdateMessageErrorComponent
        | ApiV1AlertsPartialUpdateNameErrorComponent
        | ApiV1AlertsPartialUpdateNamespaceErrorComponent
        | ApiV1AlertsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1AlertsPartialUpdatePanelUrlErrorComponent
        | ApiV1AlertsPartialUpdatePlatformServiceErrorComponent
        | ApiV1AlertsPartialUpdatePodErrorComponent
        | ApiV1AlertsPartialUpdateProviderErrorComponent
        | ApiV1AlertsPartialUpdateProviderIdErrorComponent
        | ApiV1AlertsPartialUpdateProviderReferenceErrorComponent
        | ApiV1AlertsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1AlertsPartialUpdateSilenceEndsAtErrorComponent
        | ApiV1AlertsPartialUpdateSilenceUrlErrorComponent
        | ApiV1AlertsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1AlertsPartialUpdateSlaTargetErrorComponent
        | ApiV1AlertsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1AlertsPartialUpdateSloTargetErrorComponent
        | ApiV1AlertsPartialUpdateStatusErrorComponent
        | ApiV1AlertsPartialUpdateSuppressedErrorComponent
        | ApiV1AlertsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1AlertsPartialUpdateTitleErrorComponent
        | ApiV1AlertsPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alerts_partial_update_alert_router_error_component import (
            ApiV1AlertsPartialUpdateAlertRouterErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_annotations_error_component import (
            ApiV1AlertsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_archived_at_error_component import (
            ApiV1AlertsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_archived_error_component import (
            ApiV1AlertsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_archived_reason_error_component import (
            ApiV1AlertsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_category_error_component import (
            ApiV1AlertsPartialUpdateCategoryErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_criticality_error_component import (
            ApiV1AlertsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_dashboard_url_error_component import (
            ApiV1AlertsPartialUpdateDashboardUrlErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_debug_mode_error_component import (
            ApiV1AlertsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_display_name_error_component import (
            ApiV1AlertsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_external_url_error_component import (
            ApiV1AlertsPartialUpdateExternalUrlErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_fingerprint_error_component import (
            ApiV1AlertsPartialUpdateFingerprintErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_generator_url_error_component import (
            ApiV1AlertsPartialUpdateGeneratorUrlErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_k8s_app_error_component import (
            ApiV1AlertsPartialUpdateK8SAppErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_k8s_cluster_error_component import (
            ApiV1AlertsPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_kind_error_component import (
            ApiV1AlertsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_labels_error_component import (
            ApiV1AlertsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_last_seen_error_component import (
            ApiV1AlertsPartialUpdateLastSeenErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_message_error_component import (
            ApiV1AlertsPartialUpdateMessageErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_name_error_component import (
            ApiV1AlertsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_namespace_error_component import (
            ApiV1AlertsPartialUpdateNamespaceErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_non_field_errors_error_component import (
            ApiV1AlertsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_panel_url_error_component import (
            ApiV1AlertsPartialUpdatePanelUrlErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_platform_service_error_component import (
            ApiV1AlertsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_pod_error_component import ApiV1AlertsPartialUpdatePodErrorComponent
        from ..models.api_v1_alerts_partial_update_provider_error_component import (
            ApiV1AlertsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_provider_id_error_component import (
            ApiV1AlertsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_provider_reference_error_component import (
            ApiV1AlertsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_reconciliation_enabled_error_component import (
            ApiV1AlertsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_silence_ends_at_error_component import (
            ApiV1AlertsPartialUpdateSilenceEndsAtErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_silence_url_error_component import (
            ApiV1AlertsPartialUpdateSilenceUrlErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_sla_availability_error_component import (
            ApiV1AlertsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_sla_target_error_component import (
            ApiV1AlertsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_slo_availability_error_component import (
            ApiV1AlertsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_slo_target_error_component import (
            ApiV1AlertsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_status_error_component import (
            ApiV1AlertsPartialUpdateStatusErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_suppressed_error_component import (
            ApiV1AlertsPartialUpdateSuppressedErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_target_availability_error_component import (
            ApiV1AlertsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_title_error_component import (
            ApiV1AlertsPartialUpdateTitleErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_tolerations_error_component import (
            ApiV1AlertsPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateTitleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateFingerprintErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateExternalUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateMessageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateLastSeenErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateSuppressedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdatePodErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateCategoryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateDashboardUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdatePanelUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateSilenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateSilenceEndsAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateGeneratorUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateAlertRouterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsPartialUpdateK8SAppErrorComponent):
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
        from ..models.api_v1_alerts_partial_update_alert_router_error_component import (
            ApiV1AlertsPartialUpdateAlertRouterErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_annotations_error_component import (
            ApiV1AlertsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_archived_at_error_component import (
            ApiV1AlertsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_archived_error_component import (
            ApiV1AlertsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_archived_reason_error_component import (
            ApiV1AlertsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_block_error_component import (
            ApiV1AlertsPartialUpdateBlockErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_category_error_component import (
            ApiV1AlertsPartialUpdateCategoryErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_criticality_error_component import (
            ApiV1AlertsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_dashboard_url_error_component import (
            ApiV1AlertsPartialUpdateDashboardUrlErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_debug_mode_error_component import (
            ApiV1AlertsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_display_name_error_component import (
            ApiV1AlertsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_external_url_error_component import (
            ApiV1AlertsPartialUpdateExternalUrlErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_fingerprint_error_component import (
            ApiV1AlertsPartialUpdateFingerprintErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_generator_url_error_component import (
            ApiV1AlertsPartialUpdateGeneratorUrlErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_k8s_app_error_component import (
            ApiV1AlertsPartialUpdateK8SAppErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_k8s_cluster_error_component import (
            ApiV1AlertsPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_kind_error_component import (
            ApiV1AlertsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_labels_error_component import (
            ApiV1AlertsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_last_seen_error_component import (
            ApiV1AlertsPartialUpdateLastSeenErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_message_error_component import (
            ApiV1AlertsPartialUpdateMessageErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_name_error_component import (
            ApiV1AlertsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_namespace_error_component import (
            ApiV1AlertsPartialUpdateNamespaceErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_non_field_errors_error_component import (
            ApiV1AlertsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_panel_url_error_component import (
            ApiV1AlertsPartialUpdatePanelUrlErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_platform_service_error_component import (
            ApiV1AlertsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_pod_error_component import ApiV1AlertsPartialUpdatePodErrorComponent
        from ..models.api_v1_alerts_partial_update_provider_error_component import (
            ApiV1AlertsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_provider_id_error_component import (
            ApiV1AlertsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_provider_reference_error_component import (
            ApiV1AlertsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_reconciliation_enabled_error_component import (
            ApiV1AlertsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_silence_ends_at_error_component import (
            ApiV1AlertsPartialUpdateSilenceEndsAtErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_silence_url_error_component import (
            ApiV1AlertsPartialUpdateSilenceUrlErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_sla_availability_error_component import (
            ApiV1AlertsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_sla_target_error_component import (
            ApiV1AlertsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_slo_availability_error_component import (
            ApiV1AlertsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_slo_target_error_component import (
            ApiV1AlertsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_status_error_component import (
            ApiV1AlertsPartialUpdateStatusErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_suppressed_error_component import (
            ApiV1AlertsPartialUpdateSuppressedErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_target_availability_error_component import (
            ApiV1AlertsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_title_error_component import (
            ApiV1AlertsPartialUpdateTitleErrorComponent,
        )
        from ..models.api_v1_alerts_partial_update_tolerations_error_component import (
            ApiV1AlertsPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertsPartialUpdateAlertRouterErrorComponent
                | ApiV1AlertsPartialUpdateAnnotationsErrorComponent
                | ApiV1AlertsPartialUpdateArchivedAtErrorComponent
                | ApiV1AlertsPartialUpdateArchivedErrorComponent
                | ApiV1AlertsPartialUpdateArchivedReasonErrorComponent
                | ApiV1AlertsPartialUpdateBlockErrorComponent
                | ApiV1AlertsPartialUpdateCategoryErrorComponent
                | ApiV1AlertsPartialUpdateCriticalityErrorComponent
                | ApiV1AlertsPartialUpdateDashboardUrlErrorComponent
                | ApiV1AlertsPartialUpdateDebugModeErrorComponent
                | ApiV1AlertsPartialUpdateDisplayNameErrorComponent
                | ApiV1AlertsPartialUpdateExternalUrlErrorComponent
                | ApiV1AlertsPartialUpdateFingerprintErrorComponent
                | ApiV1AlertsPartialUpdateGeneratorUrlErrorComponent
                | ApiV1AlertsPartialUpdateK8SAppErrorComponent
                | ApiV1AlertsPartialUpdateK8SClusterErrorComponent
                | ApiV1AlertsPartialUpdateKindErrorComponent
                | ApiV1AlertsPartialUpdateLabelsErrorComponent
                | ApiV1AlertsPartialUpdateLastSeenErrorComponent
                | ApiV1AlertsPartialUpdateMessageErrorComponent
                | ApiV1AlertsPartialUpdateNameErrorComponent
                | ApiV1AlertsPartialUpdateNamespaceErrorComponent
                | ApiV1AlertsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1AlertsPartialUpdatePanelUrlErrorComponent
                | ApiV1AlertsPartialUpdatePlatformServiceErrorComponent
                | ApiV1AlertsPartialUpdatePodErrorComponent
                | ApiV1AlertsPartialUpdateProviderErrorComponent
                | ApiV1AlertsPartialUpdateProviderIdErrorComponent
                | ApiV1AlertsPartialUpdateProviderReferenceErrorComponent
                | ApiV1AlertsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1AlertsPartialUpdateSilenceEndsAtErrorComponent
                | ApiV1AlertsPartialUpdateSilenceUrlErrorComponent
                | ApiV1AlertsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1AlertsPartialUpdateSlaTargetErrorComponent
                | ApiV1AlertsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1AlertsPartialUpdateSloTargetErrorComponent
                | ApiV1AlertsPartialUpdateStatusErrorComponent
                | ApiV1AlertsPartialUpdateSuppressedErrorComponent
                | ApiV1AlertsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1AlertsPartialUpdateTitleErrorComponent
                | ApiV1AlertsPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_0 = (
                        ApiV1AlertsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_1 = (
                        ApiV1AlertsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_2 = (
                        ApiV1AlertsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_3 = (
                        ApiV1AlertsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_4 = (
                        ApiV1AlertsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_5 = (
                        ApiV1AlertsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_6 = (
                        ApiV1AlertsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_7 = (
                        ApiV1AlertsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_8 = (
                        ApiV1AlertsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_9 = (
                        ApiV1AlertsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_10 = (
                        ApiV1AlertsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_11 = (
                        ApiV1AlertsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_12 = (
                        ApiV1AlertsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_13 = (
                        ApiV1AlertsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_14 = (
                        ApiV1AlertsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_15 = (
                        ApiV1AlertsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_16 = (
                        ApiV1AlertsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_17 = (
                        ApiV1AlertsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_18 = (
                        ApiV1AlertsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_19 = (
                        ApiV1AlertsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_20 = (
                        ApiV1AlertsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_21 = (
                        ApiV1AlertsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_22 = (
                        ApiV1AlertsPartialUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_23 = (
                        ApiV1AlertsPartialUpdateTitleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_24 = (
                        ApiV1AlertsPartialUpdateFingerprintErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_25 = (
                        ApiV1AlertsPartialUpdateExternalUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_26 = (
                        ApiV1AlertsPartialUpdateMessageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_27 = (
                        ApiV1AlertsPartialUpdateLastSeenErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_28 = (
                        ApiV1AlertsPartialUpdateSuppressedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_29 = (
                        ApiV1AlertsPartialUpdatePodErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_30 = (
                        ApiV1AlertsPartialUpdateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_31 = (
                        ApiV1AlertsPartialUpdateCategoryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_32 = (
                        ApiV1AlertsPartialUpdateDashboardUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_33 = (
                        ApiV1AlertsPartialUpdatePanelUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_34 = (
                        ApiV1AlertsPartialUpdateSilenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_35 = (
                        ApiV1AlertsPartialUpdateSilenceEndsAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_36 = (
                        ApiV1AlertsPartialUpdateGeneratorUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_37 = (
                        ApiV1AlertsPartialUpdateAlertRouterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_38 = (
                        ApiV1AlertsPartialUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_partial_update_error_type_39 = (
                        ApiV1AlertsPartialUpdateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alerts_partial_update_error_type_40 = (
                    ApiV1AlertsPartialUpdateBlockErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_alerts_partial_update_error_type_40

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alerts_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alerts_partial_update_validation_error.additional_properties = d
        return api_v1_alerts_partial_update_validation_error

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
