from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alerts_archive_create_alert_router_error_component import (
        ApiV1AlertsArchiveCreateAlertRouterErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_annotations_error_component import (
        ApiV1AlertsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_archived_at_error_component import (
        ApiV1AlertsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_archived_error_component import (
        ApiV1AlertsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_archived_reason_error_component import (
        ApiV1AlertsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_block_error_component import ApiV1AlertsArchiveCreateBlockErrorComponent
    from ..models.api_v1_alerts_archive_create_category_error_component import (
        ApiV1AlertsArchiveCreateCategoryErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_criticality_error_component import (
        ApiV1AlertsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_dashboard_url_error_component import (
        ApiV1AlertsArchiveCreateDashboardUrlErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_debug_mode_error_component import (
        ApiV1AlertsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_display_name_error_component import (
        ApiV1AlertsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_external_url_error_component import (
        ApiV1AlertsArchiveCreateExternalUrlErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_fingerprint_error_component import (
        ApiV1AlertsArchiveCreateFingerprintErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_generator_url_error_component import (
        ApiV1AlertsArchiveCreateGeneratorUrlErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_k8s_app_error_component import (
        ApiV1AlertsArchiveCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_k8s_cluster_error_component import (
        ApiV1AlertsArchiveCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_kind_error_component import ApiV1AlertsArchiveCreateKindErrorComponent
    from ..models.api_v1_alerts_archive_create_labels_error_component import (
        ApiV1AlertsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_last_seen_error_component import (
        ApiV1AlertsArchiveCreateLastSeenErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_message_error_component import (
        ApiV1AlertsArchiveCreateMessageErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_name_error_component import ApiV1AlertsArchiveCreateNameErrorComponent
    from ..models.api_v1_alerts_archive_create_namespace_error_component import (
        ApiV1AlertsArchiveCreateNamespaceErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_non_field_errors_error_component import (
        ApiV1AlertsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_panel_url_error_component import (
        ApiV1AlertsArchiveCreatePanelUrlErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_platform_service_error_component import (
        ApiV1AlertsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_pod_error_component import ApiV1AlertsArchiveCreatePodErrorComponent
    from ..models.api_v1_alerts_archive_create_provider_error_component import (
        ApiV1AlertsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_provider_id_error_component import (
        ApiV1AlertsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_provider_reference_error_component import (
        ApiV1AlertsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_reconciliation_enabled_error_component import (
        ApiV1AlertsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_silence_ends_at_error_component import (
        ApiV1AlertsArchiveCreateSilenceEndsAtErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_silence_url_error_component import (
        ApiV1AlertsArchiveCreateSilenceUrlErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_sla_availability_error_component import (
        ApiV1AlertsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_sla_target_error_component import (
        ApiV1AlertsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_slo_availability_error_component import (
        ApiV1AlertsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_slo_target_error_component import (
        ApiV1AlertsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_status_error_component import (
        ApiV1AlertsArchiveCreateStatusErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_suppressed_error_component import (
        ApiV1AlertsArchiveCreateSuppressedErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_target_availability_error_component import (
        ApiV1AlertsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alerts_archive_create_title_error_component import ApiV1AlertsArchiveCreateTitleErrorComponent
    from ..models.api_v1_alerts_archive_create_tolerations_error_component import (
        ApiV1AlertsArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AlertsArchiveCreateValidationError")


@_attrs_define
class ApiV1AlertsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertsArchiveCreateAlertRouterErrorComponent |
            ApiV1AlertsArchiveCreateAnnotationsErrorComponent | ApiV1AlertsArchiveCreateArchivedAtErrorComponent |
            ApiV1AlertsArchiveCreateArchivedErrorComponent | ApiV1AlertsArchiveCreateArchivedReasonErrorComponent |
            ApiV1AlertsArchiveCreateBlockErrorComponent | ApiV1AlertsArchiveCreateCategoryErrorComponent |
            ApiV1AlertsArchiveCreateCriticalityErrorComponent | ApiV1AlertsArchiveCreateDashboardUrlErrorComponent |
            ApiV1AlertsArchiveCreateDebugModeErrorComponent | ApiV1AlertsArchiveCreateDisplayNameErrorComponent |
            ApiV1AlertsArchiveCreateExternalUrlErrorComponent | ApiV1AlertsArchiveCreateFingerprintErrorComponent |
            ApiV1AlertsArchiveCreateGeneratorUrlErrorComponent | ApiV1AlertsArchiveCreateK8SAppErrorComponent |
            ApiV1AlertsArchiveCreateK8SClusterErrorComponent | ApiV1AlertsArchiveCreateKindErrorComponent |
            ApiV1AlertsArchiveCreateLabelsErrorComponent | ApiV1AlertsArchiveCreateLastSeenErrorComponent |
            ApiV1AlertsArchiveCreateMessageErrorComponent | ApiV1AlertsArchiveCreateNameErrorComponent |
            ApiV1AlertsArchiveCreateNamespaceErrorComponent | ApiV1AlertsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1AlertsArchiveCreatePanelUrlErrorComponent | ApiV1AlertsArchiveCreatePlatformServiceErrorComponent |
            ApiV1AlertsArchiveCreatePodErrorComponent | ApiV1AlertsArchiveCreateProviderErrorComponent |
            ApiV1AlertsArchiveCreateProviderIdErrorComponent | ApiV1AlertsArchiveCreateProviderReferenceErrorComponent |
            ApiV1AlertsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1AlertsArchiveCreateSilenceEndsAtErrorComponent | ApiV1AlertsArchiveCreateSilenceUrlErrorComponent |
            ApiV1AlertsArchiveCreateSlaAvailabilityErrorComponent | ApiV1AlertsArchiveCreateSlaTargetErrorComponent |
            ApiV1AlertsArchiveCreateSloAvailabilityErrorComponent | ApiV1AlertsArchiveCreateSloTargetErrorComponent |
            ApiV1AlertsArchiveCreateStatusErrorComponent | ApiV1AlertsArchiveCreateSuppressedErrorComponent |
            ApiV1AlertsArchiveCreateTargetAvailabilityErrorComponent | ApiV1AlertsArchiveCreateTitleErrorComponent |
            ApiV1AlertsArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertsArchiveCreateAlertRouterErrorComponent
        | ApiV1AlertsArchiveCreateAnnotationsErrorComponent
        | ApiV1AlertsArchiveCreateArchivedAtErrorComponent
        | ApiV1AlertsArchiveCreateArchivedErrorComponent
        | ApiV1AlertsArchiveCreateArchivedReasonErrorComponent
        | ApiV1AlertsArchiveCreateBlockErrorComponent
        | ApiV1AlertsArchiveCreateCategoryErrorComponent
        | ApiV1AlertsArchiveCreateCriticalityErrorComponent
        | ApiV1AlertsArchiveCreateDashboardUrlErrorComponent
        | ApiV1AlertsArchiveCreateDebugModeErrorComponent
        | ApiV1AlertsArchiveCreateDisplayNameErrorComponent
        | ApiV1AlertsArchiveCreateExternalUrlErrorComponent
        | ApiV1AlertsArchiveCreateFingerprintErrorComponent
        | ApiV1AlertsArchiveCreateGeneratorUrlErrorComponent
        | ApiV1AlertsArchiveCreateK8SAppErrorComponent
        | ApiV1AlertsArchiveCreateK8SClusterErrorComponent
        | ApiV1AlertsArchiveCreateKindErrorComponent
        | ApiV1AlertsArchiveCreateLabelsErrorComponent
        | ApiV1AlertsArchiveCreateLastSeenErrorComponent
        | ApiV1AlertsArchiveCreateMessageErrorComponent
        | ApiV1AlertsArchiveCreateNameErrorComponent
        | ApiV1AlertsArchiveCreateNamespaceErrorComponent
        | ApiV1AlertsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1AlertsArchiveCreatePanelUrlErrorComponent
        | ApiV1AlertsArchiveCreatePlatformServiceErrorComponent
        | ApiV1AlertsArchiveCreatePodErrorComponent
        | ApiV1AlertsArchiveCreateProviderErrorComponent
        | ApiV1AlertsArchiveCreateProviderIdErrorComponent
        | ApiV1AlertsArchiveCreateProviderReferenceErrorComponent
        | ApiV1AlertsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1AlertsArchiveCreateSilenceEndsAtErrorComponent
        | ApiV1AlertsArchiveCreateSilenceUrlErrorComponent
        | ApiV1AlertsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1AlertsArchiveCreateSlaTargetErrorComponent
        | ApiV1AlertsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1AlertsArchiveCreateSloTargetErrorComponent
        | ApiV1AlertsArchiveCreateStatusErrorComponent
        | ApiV1AlertsArchiveCreateSuppressedErrorComponent
        | ApiV1AlertsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1AlertsArchiveCreateTitleErrorComponent
        | ApiV1AlertsArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alerts_archive_create_alert_router_error_component import (
            ApiV1AlertsArchiveCreateAlertRouterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_annotations_error_component import (
            ApiV1AlertsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_archived_at_error_component import (
            ApiV1AlertsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_archived_error_component import (
            ApiV1AlertsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_archived_reason_error_component import (
            ApiV1AlertsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_category_error_component import (
            ApiV1AlertsArchiveCreateCategoryErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_criticality_error_component import (
            ApiV1AlertsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_dashboard_url_error_component import (
            ApiV1AlertsArchiveCreateDashboardUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_debug_mode_error_component import (
            ApiV1AlertsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_display_name_error_component import (
            ApiV1AlertsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_external_url_error_component import (
            ApiV1AlertsArchiveCreateExternalUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_fingerprint_error_component import (
            ApiV1AlertsArchiveCreateFingerprintErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_generator_url_error_component import (
            ApiV1AlertsArchiveCreateGeneratorUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_k8s_app_error_component import (
            ApiV1AlertsArchiveCreateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_k8s_cluster_error_component import (
            ApiV1AlertsArchiveCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_kind_error_component import (
            ApiV1AlertsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_labels_error_component import (
            ApiV1AlertsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_last_seen_error_component import (
            ApiV1AlertsArchiveCreateLastSeenErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_message_error_component import (
            ApiV1AlertsArchiveCreateMessageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_name_error_component import (
            ApiV1AlertsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_namespace_error_component import (
            ApiV1AlertsArchiveCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_non_field_errors_error_component import (
            ApiV1AlertsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_panel_url_error_component import (
            ApiV1AlertsArchiveCreatePanelUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_platform_service_error_component import (
            ApiV1AlertsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_pod_error_component import (
            ApiV1AlertsArchiveCreatePodErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_provider_error_component import (
            ApiV1AlertsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_provider_id_error_component import (
            ApiV1AlertsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_provider_reference_error_component import (
            ApiV1AlertsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_reconciliation_enabled_error_component import (
            ApiV1AlertsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_silence_ends_at_error_component import (
            ApiV1AlertsArchiveCreateSilenceEndsAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_silence_url_error_component import (
            ApiV1AlertsArchiveCreateSilenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_sla_availability_error_component import (
            ApiV1AlertsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_sla_target_error_component import (
            ApiV1AlertsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_slo_availability_error_component import (
            ApiV1AlertsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_slo_target_error_component import (
            ApiV1AlertsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_status_error_component import (
            ApiV1AlertsArchiveCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_suppressed_error_component import (
            ApiV1AlertsArchiveCreateSuppressedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_target_availability_error_component import (
            ApiV1AlertsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_title_error_component import (
            ApiV1AlertsArchiveCreateTitleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_tolerations_error_component import (
            ApiV1AlertsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateTitleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateFingerprintErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateExternalUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateMessageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateLastSeenErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateSuppressedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreatePodErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateCategoryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateDashboardUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreatePanelUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateSilenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateSilenceEndsAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateGeneratorUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateAlertRouterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertsArchiveCreateK8SAppErrorComponent):
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
        from ..models.api_v1_alerts_archive_create_alert_router_error_component import (
            ApiV1AlertsArchiveCreateAlertRouterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_annotations_error_component import (
            ApiV1AlertsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_archived_at_error_component import (
            ApiV1AlertsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_archived_error_component import (
            ApiV1AlertsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_archived_reason_error_component import (
            ApiV1AlertsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_block_error_component import (
            ApiV1AlertsArchiveCreateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_category_error_component import (
            ApiV1AlertsArchiveCreateCategoryErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_criticality_error_component import (
            ApiV1AlertsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_dashboard_url_error_component import (
            ApiV1AlertsArchiveCreateDashboardUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_debug_mode_error_component import (
            ApiV1AlertsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_display_name_error_component import (
            ApiV1AlertsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_external_url_error_component import (
            ApiV1AlertsArchiveCreateExternalUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_fingerprint_error_component import (
            ApiV1AlertsArchiveCreateFingerprintErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_generator_url_error_component import (
            ApiV1AlertsArchiveCreateGeneratorUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_k8s_app_error_component import (
            ApiV1AlertsArchiveCreateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_k8s_cluster_error_component import (
            ApiV1AlertsArchiveCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_kind_error_component import (
            ApiV1AlertsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_labels_error_component import (
            ApiV1AlertsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_last_seen_error_component import (
            ApiV1AlertsArchiveCreateLastSeenErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_message_error_component import (
            ApiV1AlertsArchiveCreateMessageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_name_error_component import (
            ApiV1AlertsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_namespace_error_component import (
            ApiV1AlertsArchiveCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_non_field_errors_error_component import (
            ApiV1AlertsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_panel_url_error_component import (
            ApiV1AlertsArchiveCreatePanelUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_platform_service_error_component import (
            ApiV1AlertsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_pod_error_component import (
            ApiV1AlertsArchiveCreatePodErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_provider_error_component import (
            ApiV1AlertsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_provider_id_error_component import (
            ApiV1AlertsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_provider_reference_error_component import (
            ApiV1AlertsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_reconciliation_enabled_error_component import (
            ApiV1AlertsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_silence_ends_at_error_component import (
            ApiV1AlertsArchiveCreateSilenceEndsAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_silence_url_error_component import (
            ApiV1AlertsArchiveCreateSilenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_sla_availability_error_component import (
            ApiV1AlertsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_sla_target_error_component import (
            ApiV1AlertsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_slo_availability_error_component import (
            ApiV1AlertsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_slo_target_error_component import (
            ApiV1AlertsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_status_error_component import (
            ApiV1AlertsArchiveCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_suppressed_error_component import (
            ApiV1AlertsArchiveCreateSuppressedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_target_availability_error_component import (
            ApiV1AlertsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_title_error_component import (
            ApiV1AlertsArchiveCreateTitleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alerts_archive_create_tolerations_error_component import (
            ApiV1AlertsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertsArchiveCreateAlertRouterErrorComponent
                | ApiV1AlertsArchiveCreateAnnotationsErrorComponent
                | ApiV1AlertsArchiveCreateArchivedAtErrorComponent
                | ApiV1AlertsArchiveCreateArchivedErrorComponent
                | ApiV1AlertsArchiveCreateArchivedReasonErrorComponent
                | ApiV1AlertsArchiveCreateBlockErrorComponent
                | ApiV1AlertsArchiveCreateCategoryErrorComponent
                | ApiV1AlertsArchiveCreateCriticalityErrorComponent
                | ApiV1AlertsArchiveCreateDashboardUrlErrorComponent
                | ApiV1AlertsArchiveCreateDebugModeErrorComponent
                | ApiV1AlertsArchiveCreateDisplayNameErrorComponent
                | ApiV1AlertsArchiveCreateExternalUrlErrorComponent
                | ApiV1AlertsArchiveCreateFingerprintErrorComponent
                | ApiV1AlertsArchiveCreateGeneratorUrlErrorComponent
                | ApiV1AlertsArchiveCreateK8SAppErrorComponent
                | ApiV1AlertsArchiveCreateK8SClusterErrorComponent
                | ApiV1AlertsArchiveCreateKindErrorComponent
                | ApiV1AlertsArchiveCreateLabelsErrorComponent
                | ApiV1AlertsArchiveCreateLastSeenErrorComponent
                | ApiV1AlertsArchiveCreateMessageErrorComponent
                | ApiV1AlertsArchiveCreateNameErrorComponent
                | ApiV1AlertsArchiveCreateNamespaceErrorComponent
                | ApiV1AlertsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1AlertsArchiveCreatePanelUrlErrorComponent
                | ApiV1AlertsArchiveCreatePlatformServiceErrorComponent
                | ApiV1AlertsArchiveCreatePodErrorComponent
                | ApiV1AlertsArchiveCreateProviderErrorComponent
                | ApiV1AlertsArchiveCreateProviderIdErrorComponent
                | ApiV1AlertsArchiveCreateProviderReferenceErrorComponent
                | ApiV1AlertsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1AlertsArchiveCreateSilenceEndsAtErrorComponent
                | ApiV1AlertsArchiveCreateSilenceUrlErrorComponent
                | ApiV1AlertsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1AlertsArchiveCreateSlaTargetErrorComponent
                | ApiV1AlertsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1AlertsArchiveCreateSloTargetErrorComponent
                | ApiV1AlertsArchiveCreateStatusErrorComponent
                | ApiV1AlertsArchiveCreateSuppressedErrorComponent
                | ApiV1AlertsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1AlertsArchiveCreateTitleErrorComponent
                | ApiV1AlertsArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_0 = (
                        ApiV1AlertsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_1 = (
                        ApiV1AlertsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_2 = (
                        ApiV1AlertsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_3 = (
                        ApiV1AlertsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_4 = (
                        ApiV1AlertsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_5 = (
                        ApiV1AlertsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_6 = (
                        ApiV1AlertsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_7 = (
                        ApiV1AlertsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_8 = (
                        ApiV1AlertsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_9 = (
                        ApiV1AlertsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_10 = (
                        ApiV1AlertsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_11 = (
                        ApiV1AlertsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_12 = (
                        ApiV1AlertsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_13 = (
                        ApiV1AlertsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_14 = (
                        ApiV1AlertsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_15 = (
                        ApiV1AlertsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_16 = (
                        ApiV1AlertsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_17 = (
                        ApiV1AlertsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_18 = (
                        ApiV1AlertsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_19 = (
                        ApiV1AlertsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_20 = (
                        ApiV1AlertsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_21 = (
                        ApiV1AlertsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_22 = (
                        ApiV1AlertsArchiveCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_23 = (
                        ApiV1AlertsArchiveCreateTitleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_24 = (
                        ApiV1AlertsArchiveCreateFingerprintErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_25 = (
                        ApiV1AlertsArchiveCreateExternalUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_26 = (
                        ApiV1AlertsArchiveCreateMessageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_27 = (
                        ApiV1AlertsArchiveCreateLastSeenErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_28 = (
                        ApiV1AlertsArchiveCreateSuppressedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_29 = (
                        ApiV1AlertsArchiveCreatePodErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_30 = (
                        ApiV1AlertsArchiveCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_31 = (
                        ApiV1AlertsArchiveCreateCategoryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_32 = (
                        ApiV1AlertsArchiveCreateDashboardUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_33 = (
                        ApiV1AlertsArchiveCreatePanelUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_34 = (
                        ApiV1AlertsArchiveCreateSilenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_35 = (
                        ApiV1AlertsArchiveCreateSilenceEndsAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_36 = (
                        ApiV1AlertsArchiveCreateGeneratorUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_37 = (
                        ApiV1AlertsArchiveCreateAlertRouterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_38 = (
                        ApiV1AlertsArchiveCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alerts_archive_create_error_type_39 = (
                        ApiV1AlertsArchiveCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alerts_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alerts_archive_create_error_type_40 = (
                    ApiV1AlertsArchiveCreateBlockErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_alerts_archive_create_error_type_40

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alerts_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alerts_archive_create_validation_error.additional_properties = d
        return api_v1_alerts_archive_create_validation_error

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
