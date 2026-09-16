from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_actual_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_addon_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAddonErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_annotations_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_archived_at_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_archived_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_archived_reason_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_block_config_template_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_block_name_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_criticality_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_debug_mode_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_discovery_enabled_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_display_name_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_k8s_cluster_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_kind_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_labels_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_name_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_non_field_errors_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_order_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateOrderErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_platform_service_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_provider_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_provider_id_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_provider_reference_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_scope_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_sla_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_sla_target_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_slo_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_slo_target_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_target_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_version_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateValidationError")


@_attrs_define
class ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAddonErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAnnotationsErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedAtErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockConfigTemplateErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockNameErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateCriticalityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDebugModeErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDisplayNameErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateK8SClusterErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateKindErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateLabelsErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNameErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateOrderErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdatePlatformServiceErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderIdErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateScopeErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaTargetErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloTargetErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAddonErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAnnotationsErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedAtErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockConfigTemplateErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockNameErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateCriticalityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDebugModeErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDisplayNameErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateK8SClusterErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateKindErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateLabelsErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNameErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateOrderErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderIdErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateScopeErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaTargetErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloTargetErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_actual_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_addon_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAddonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_annotations_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_archived_at_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_archived_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_archived_reason_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_block_config_template_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_block_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_criticality_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_debug_mode_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_display_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_k8s_cluster_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_kind_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_labels_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_platform_service_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_provider_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_provider_id_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_provider_reference_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_scope_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_sla_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_sla_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_slo_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_slo_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_target_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_version_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateVersionErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNonFieldErrorsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDisplayNameErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateLabelsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAnnotationsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDebugModeErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderReferenceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderIdErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data,
                ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateReconciliationEnabledErrorComponent,
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDiscoveryEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdatePlatformServiceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedAtErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedReasonErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateCriticalityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateActualAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloTargetErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaTargetErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateK8SClusterErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAddonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateVersionErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockNameErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockConfigTemplateErrorComponent
            ):
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
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_actual_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_addon_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAddonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_annotations_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_archived_at_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_archived_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_archived_reason_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_block_config_template_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_block_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_criticality_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_debug_mode_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_display_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_k8s_cluster_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_kind_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_labels_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_order_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateOrderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_platform_service_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_provider_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_provider_id_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_provider_reference_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_scope_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_sla_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_sla_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_slo_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_slo_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_target_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_partial_update_version_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateVersionErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAddonErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAnnotationsErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedAtErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockConfigTemplateErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockNameErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateCriticalityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDebugModeErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDisplayNameErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateK8SClusterErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateKindErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateLabelsErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNameErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateOrderErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderIdErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateScopeErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaTargetErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloTargetErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_0 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNonFieldErrorsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_1 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_2 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_3 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_4 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_5 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_6 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_7 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderReferenceErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_8 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_9 = ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateReconciliationEnabledErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_10 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateDiscoveryEnabledErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_11 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdatePlatformServiceErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_12 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_13 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_14 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_15 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_16 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateArchivedReasonErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_17 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_18 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateTargetAvailabilityErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_19 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateActualAvailabilityErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_20 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_21 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSloAvailabilityErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_22 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_23 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateSlaAvailabilityErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_24 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_25 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateAddonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_26 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_27 = (
                        ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_28 = ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateBlockConfigTemplateErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_29 = (
                    ApiV1KubernetesClusterAddonSubscriptionsPartialUpdateOrderErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_partial_update_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_cluster_addon_subscriptions_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_cluster_addon_subscriptions_partial_update_validation_error.additional_properties = d
        return api_v1_kubernetes_cluster_addon_subscriptions_partial_update_validation_error

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
